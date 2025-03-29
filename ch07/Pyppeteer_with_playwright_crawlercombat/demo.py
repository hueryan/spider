from playwright.async_api import async_playwright
from playwright.async_api import TimeoutError
from playwright.async_api import Page, Browser
import logging
import asyncio
import json
from os import makedirs
from os.path import exists

RESULTS_DIR = 'results'

exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

INDEX_URL = 'https://spa2.scrape.center/page/{page}'
TIME_OUT = 10
TOTAL_PAGE = 10
WINDOW_WIDTH, WINDOW_HEIGHT = 1366, 768
HEADLESS = False

# 通用爬取方法
# url 爬取页面，selector等待渲染出的节点对应的CSS选择器。
async def scrape_page(url, selector):
    logging.info('scraping %s', url)
    try:
        await tab.goto(url)
        await tab.wait_for_selector(selector, timeout=TIME_OUT * 1000)
    except TimeoutError:
        logging.error('error occurred while scraping %s', url, exc_info=True)

# 爬取列表页
async def scrape_index(page):
    url = INDEX_URL.format(page=page)
    await scrape_page(url, '.item .name')

# 解析列表页，用来提取每部电影的详细页URL
async def parse_index():
    # selector选择器。
    # pageFunction，执行JS方法。找出和选择器匹配的节点，根据pagefunction定义的逻辑从这些节点中抽取出对应的结果并返回
    return await tab.eval_on_selector_all('.item .name', 'nodes => nodes.map(node => node.href)')

# 爬取每个详情页
async def scrape_detail(url):
    await scrape_page(url, 'h2')

# 提取详情页信息
async def parse_detail():
    url = tab.url
    name = await tab.eval_on_selector('h2', 'node => node.innerText')
    categories = await tab.eval_on_selector_all('.categoried button span', 'nodes => nodes.map(node => node.innerText)')
    cover = await tab.eval_on_selector('.cover', 'node => node.src')
    score = await tab.eval_on_selector('.score', 'node => node.innerText')
    drama = await tab.eval_on_selector('.drama p', 'node => node.innerText')

    return {
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }

async def save_data(data):
    name = data.get("name")
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

async def main():
    async with async_playwright() as p:
        global browser, tab
        # 浏览器对象，新建的页面选项卡
        browser = await p.chromium.launch(headless=HEADLESS, args=['--disable-infobars',
                                                                   f'--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}'])
        tab = await browser.new_page()
        await tab.set_viewport_size({'width': WINDOW_WIDTH, 'height': WINDOW_HEIGHT})

        try:
            for page in range(1, TOTAL_PAGE + 1):
                await scrape_index(page)
                detail_urls = await parse_index()
                logging.info("detail_urls %s", detail_urls)
                for detail_url in detail_urls:
                    await scrape_detail(detail_url)
                    detail_date = await parse_detail()
                    logging.info('data %s', detail_date)
                    await save_data(detail_date)
        finally:
            await browser.close()


if __name__ == '__main__':
    asyncio.run(main())






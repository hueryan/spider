from playwright.async_api import async_playwright
from playwright.async_api import TimeoutError
from playwright.async_api import Page, Browser
import logging
import asyncio


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

INDEX_URL = 'https://spa2.scrape.center/page/{page}'
TIME_OUT = 10
TOTAL_PAGE = 10
WINDOW_WIDTH, WINDOW_HEIGHT = 1366, 768
HEADLESS = False

# 通用爬取方法
# url 爬取页面，selector等待渲染出的节点对应的CSS选择器。
async def scrape_page(page: Page, url: str, selector: str):
    logging.info('scraping %s', url)
    try:
        await page.goto(url)
        await page.wait_for_selector(selector, timeout=TIME_OUT * 1000)
    except TimeoutError:
        logging.error('error occurred while scraping %s', url, exc_info=True)

# 爬取列表页
async def scrape_index(page: Page, page_num: int):
    url = INDEX_URL.format(page=page_num)
    await scrape_page(page, url, '.item .name')

# 解析列表页，用来提取每部电影的详细页URL
async def parse_index(page: Page):
    # selector选择器。
    # pageFunction，执行JS方法。找出和选择器匹配的节点，根据pagefunction定义的逻辑从这些节点中抽取出对应的结果并返回
    return await page.eval_on_selector_all('.item .name', 'nodes => nodes.map(node => node.href)')

async def main():
    async with async_playwright() as p:

        # 浏览器对象，新建的页面选项卡
        browser = await p.chromium.launch(headless=HEADLESS, args=['--disable-infobars',
                                                                   f'--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}'])
        tab = await browser.new_page()
        await tab.set_viewport_size({'width': WINDOW_WIDTH, 'height': WINDOW_HEIGHT})

        try:
            for page in range(1, TOTAL_PAGE + 1):
                await scrape_index(tab, page)
                detail_urls = await parse_index(tab)
                logging.info("detail_urls %s", detail_urls)
        finally:
            await browser.close()


if __name__ == '__main__':
    asyncio.run(main())






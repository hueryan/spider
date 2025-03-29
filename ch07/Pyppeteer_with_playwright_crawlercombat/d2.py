from d1 import scrape_page, scrape_index, parse_index
from d1 import HEADLESS, WINDOW_WIDTH, WINDOW_HEIGHT, TOTAL_PAGE
from playwright.async_api import async_playwright
from playwright.async_api import Page
import logging
import asyncio

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# 爬取每个详情页
async def scrape_detail(page: Page, url: str):
    await scrape_page(page, url, 'h2')

# 提取详情页信息
async def parse_page(page: Page):
    name = await page.eval_on_selector('h2', 'node => node.innerText')
    categories = await page.eval_on_selector_all('.categories button span', 'nodes => nodes.map(node => node.innerText)')
    cover = await page.eval_on_selector('.cover', 'node => node.src')
    score = await page.eval_on_selector('.score', 'node => node.innerText')
    drama = await page.eval_on_selector('.drama p', 'node => node.innerText')

    return {
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }

async def main():
    async with async_playwright() as p:
        # 浏览器对象，新建的页面选项卡
        browser = await p.chromium.launch(headless=HEADLESS, args=['--disable-infobars',
                                                                   f'--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}'])
        tab = await browser.new_page()
        await tab.set_viewport_size({'width': WINDOW_WIDTH, 'height': WINDOW_HEIGHT})

        try:
            for page_num in range(1, TOTAL_PAGE + 1):
                await scrape_index(tab, page_num)
                detail_urls = await parse_index(tab)
                for detail_url in detail_urls:
                    await scrape_detail(tab, detail_url)
                    detail_date = await parse_page(tab)
                    logging.info('data %s', detail_date)
        finally:
            await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
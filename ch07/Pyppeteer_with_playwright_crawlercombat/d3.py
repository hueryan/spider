from d2 import *
import json
from os import makedirs
from os.path import exists

RESULTS_DIR = 'results'

exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

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
            for page_num in range(1, TOTAL_PAGE + 1):
                await scrape_index(tab, page_num)
                detail_urls = await parse_index(tab)
                for detail_url in detail_urls:
                    await scrape_detail(tab, detail_url)
                    detail_date = await parse_page(tab)
                    logging.info('data %s', detail_date)
                    await save_data(detail_date)
        finally:
            await browser.close()


if __name__ == '__main__':
    asyncio.run(main())



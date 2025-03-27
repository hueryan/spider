import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://spa2.scrape.center')
        await page.wait_for_selector('.item .name')
        await page.click('.item .name',
                         button='right',  # 右键点击
                         click_count=1, # 1 单击 或 2 双击
                         delay=3000,  # 延迟 3 秒后释放（单位：毫秒）
        )
        await browser.close()

asyncio.run(main())
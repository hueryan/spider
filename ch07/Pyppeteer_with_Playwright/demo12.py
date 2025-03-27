import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.taobao.com')
        await page.type('#q', 'iPad')
        await asyncio.sleep(2)
        await browser.close()


asyncio.run(main())
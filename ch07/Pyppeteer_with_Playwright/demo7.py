import asyncio
from playwright.async_api import async_playwright

width, height = 1200, 768

async def main():
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False, args=['--disable-infobars', f'--window-size={width},{height}',])
        # create a new incognito browser context.
        context = await browser.new_context()
        # create a new page in a pristine context.
        page = await context.new_page()
        await page.goto('https://www.baidu.com')
        await asyncio.sleep(500)


        await context.close()
        await browser.close()

asyncio.run(main())


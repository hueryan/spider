import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto('https://spa2.scrape.center')
        print('HTML:', await page.content())
        print('Cookie:', await context.cookies())
        await browser.close()

asyncio.run(main())
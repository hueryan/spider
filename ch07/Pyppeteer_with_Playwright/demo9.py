import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        # 显式创建一个 BrowserContext（浏览器上下文）
        context = await browser.new_context()

        page = await context.new_page()
        await page.goto('https://www.baidu.com')
        page = await context.new_page()
        await page.goto('https://www.bing.com')
        pages = context.pages
        print('Pages:' ,pages)
        await asyncio.sleep(3)
        # 切换网页
        await pages[0].bring_to_front()
        await asyncio.sleep(5)

asyncio.run(main())
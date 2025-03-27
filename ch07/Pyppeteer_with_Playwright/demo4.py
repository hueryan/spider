import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:


        # 无头模式，默认 True
        # browser = await p.chromium.launch(headless=False)
        # 打开调试页面
        # browser = await p.chromium.launch(headless=False, devtools=True)
        # 禁用提示条
        browser = await p.chromium.launch(headless=False, args=['--disable-infobars'])


        # 新建一个网页
        page = await browser.new_page()
        await page.goto('https://www.baidu.com/')
        await asyncio.sleep(8)

asyncio.run(main())
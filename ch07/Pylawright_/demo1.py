# 同步
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        # 返回 Browser 对象
        browser = browser_type.launch(headless=False)
        # 新建选项卡，=> Page 对象
        page = browser.new_page()
        # 加载网页
        page.goto('https://www.baidu.com')
        page.screenshot(path=f'screenshot-sync-{browser_type.name}.png')
        # 返回页面标题
        print(page.title())
        # 关闭整个浏览器
        browser.close()

# 异步
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch(headless=False)
            page = await browser.new_page()
            await page.goto('https://www.baidu.com')
            await page.screenshot(path=f'screenshot-async-{browser_type.name}.png')
            print(await page.title())
            await page.close()

asyncio.run(main())
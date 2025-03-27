# # pyppeteer
# import asyncio
# from pyppeteer import launch
#
# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto('https://www.baidu.com')
#     await page.screenshot({'path': 'baidu.png'})
#     await browser.close()
#
# asyncio.get_event_loop().run_until_complete(main())



# 异步
import asyncio
from playwright.async_api import async_playwright  # 异步API

async def main():
    async with async_playwright() as p:  # 自动管理Playwright生命周期
        browser = await p.chromium.launch(headless=False)  # 启动Chromium（默认headless=True）
        page = await browser.new_page() # 新建页面
        await page.goto('https://www.baidu.com')  # 导航到百度
        await page.screenshot(path='baidu.png')   # 截图保存
        await browser.close()  # 关闭浏览器

asyncio.run(main())


# 同步
# from playwright.sync_api import sync_playwright  # 同步API
#
# with sync_playwright() as p:  # 自动管理Playwright生命周期
#     browser = p.chromium.launch()  # 启动浏览器
#     page = browser.new_page()      # 新建页面
#     page.goto('https://www.baidu.com')  # 导航
#     page.screenshot(path='baidu.png')   # 截图
#     browser.close()                # 关闭

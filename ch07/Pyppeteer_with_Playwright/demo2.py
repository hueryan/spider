import asyncio
from playwright.async_api import async_playwright

width, height = 1366, 768

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        try:
            # 创建页面时直接设置视窗大小
            # page = await browser.new_page(viewport={"width": width, "height": height})
            page = await browser.new_page()
            # 设置页面窗口大小
            await page.set_viewport_size({'width': width, 'height': height})
            await page.goto('https://spa2.scrape.center/')
            await page.wait_for_selector('.item .name')
            await asyncio.sleep(2)
            # 保存页面截图
            '''
            screenshot
            参数：
                path： 截图保存路径
                type：保存格式
                quality：清晰度
                full_page：是否全屏
                clip：裁切
            '''
            await page.screenshot(path='example.png')
            # 执行JS脚本，返回对应数据
            dimensions = await page.evaluate('''() => {
                return {
                    width: document.documentElement.clientWidth,
                    height: document.documentElement.clientHeight,
                    deviceScaleFactor: window.devicePixelRatio,
                }
            }''')
            print(dimensions)
        finally:
            await browser.close()

asyncio.run(main())

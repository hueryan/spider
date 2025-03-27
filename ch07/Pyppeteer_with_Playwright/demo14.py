import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.set_viewport_size({'width': 1920, 'height': 1080})
        await page.goto('https://spa2.scrape.center')
        await page.wait_for_selector('.item .name')
        await asyncio.sleep(2)
        await page.screenshot(path='example.png')
        # 执行js脚本
        dimensions = await page.evaluate('''()=>{
            return{
                width: document.documentElement.clientWidth,
                height: document.documentElement.clientHeight,
                deviceScaleFactor: window.devicePixelRatio,
            }
        }''')
        # page.expose_function()
        # page.evaluate_handle()

        print(dimensions)
        await browser.close()

asyncio.run(main())
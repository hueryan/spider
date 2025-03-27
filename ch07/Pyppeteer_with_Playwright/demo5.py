import asyncio
from playwright.async_api import async_playwright

width, height = 1366, 768

async def main():
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False, args=['--disable-infobars', f'--window-size={width}x{height}'])
        page = await browser.new_page()
        # 每次加载网页时执行某条语句,可以隐藏Wibdriver属性
        await page.set_viewport_size({'width': width, 'height': height})
        await page.add_init_script('Object.defineProperty(navigator, "webdriver", {get:()=> undefined})')
        await page.goto('https://antispider1.scrape.center')
        await asyncio.sleep(10)

asyncio.run(main())
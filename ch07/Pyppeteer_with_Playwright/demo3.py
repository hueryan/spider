from playwright.async_api import async_playwright
# from pyppeteer import launch
import asyncio

async def main():
    '''
    # browser = await launch()

    browser = await launch(
        headless=False,
        args=['--start-maximized'],
        executablePath='/path/to/chrome',
    )
    :return:
    '''


    async with async_playwright() as p:
        # browser = await p.chromium.launch()
        browser = await p.chromium.launch(
            headless=False,
            args=['--start-maximized'],
            executable_path='/path/to/chrome',  # 注意参数名改为下划线风格
        )

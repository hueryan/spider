import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://spa2.scrape.center')
        await page.wait_for_selector('.item .name')

        # 方式 1: 直接获取 ElementHandle
        j_result1 = await page.query_selector('.item .name')

        # 方式 2: 使用 Locator 并操作元素
        # j_result2_locator = page.locator('.item .name').first
        j_result2_locator = page.locator('.item .name').nth(0)

        # 获取所有元素
        jj_result1 = await page.query_selector_all('.item .name')
        jj_result2 = await page.locator('.item .name').all()  # 需要 await

        # 打印结果
        print('J Result1 (ElementHandle):', j_result1)
        print('J Result2 (Locator):', j_result2_locator)
        print('Locator1 Result (All ElementHandles):', jj_result1)
        print('Locator2 Result (All Locators):', jj_result2)

        await browser.close()


asyncio.run(main())
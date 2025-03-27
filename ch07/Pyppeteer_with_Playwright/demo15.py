import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.taobao.com')
        await page.wait_for_selector('.user-info')  # 等待某些符合条件的节点加载出来再返回结果，否则等待直到超时
        await page.wait_for_function()  # 等待某个JS方法执行完毕或返回结果

# waitForNavigation
# await page.waitForNavigation({ waitUntil: 'networkidle0' });

# # 方式 1：等待 URL 匹配（推荐）
# await page.wait_for_url("https://example.com/**", wait_until="networkidle")
#
# # 方式 2：通用导航等待
# async with page.expect_navigation(wait_until="networkidle"):
#     await page.click("a.submit")




# waitForRequest
# await page.waitForRequest(requestUrl => requestUrl.includes('/api/data'));

# # 等待包含特定 URL 的请求
# request = await page.wait_for_request(lambda req: "/api/data" in req.url)
#
# # 直接匹配 URL（简化）
# request = await page.wait_for_request("**/api/data*")




# waitForResponse
# await page.waitForResponse(response => response.url().includes('/api/data'));

# # 等待包含特定 URL 的响应
# response = await page.wait_for_response(lambda res: "/api/data" in res.url)
#
# # 直接匹配 URL（简化）
# response = await page.wait_for_response("**/api/data*")

# waitFor
# 用途：通用等待（时间、条件或元素）。
# 场景 1：固定时间等待

# # Puppeteer
# await page.waitFor(3000);

# # Playwright
# await page.wait_for_timeout(3000)  # 单位：毫秒

# 场景 2：等待条件成立
# # Puppeteer
# await page.waitFor(() => document.readyState === 'complete');

# # Playwright
# await page.wait_for_function("() => document.readyState === 'complete'")
# 场景 3：等待元素出现
# # Puppeteer
# await page.waitFor('.item');

# # Playwright
# await page.wait_for_selector('.item')
# waitForXPath


import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # 等待导航到目标页
        await page.goto('https://example.com', wait_until="networkidle")

        # 等待 API 请求并捕获响应
        async with page.expect_response("**/api/data") as resp_info:
            await page.click("#fetch-data")
        response = await resp_info.value
        print("响应数据:", await response.json())

        # 等待 XPath 元素可见
        await page.wait_for_selector('xpath=//div[@class="item"]', state="visible")

        await browser.close()


asyncio.run(main())
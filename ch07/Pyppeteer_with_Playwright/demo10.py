import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.baidu.com')
        # await asyncio.sleep(2)
        await page.goto('https://spa2.scrape.center')
        # await asyncio.sleep(2)
        # 后退
        await page.go_back()
        # await asyncio.sleep(2)
        # 前进
        await page.go_forward()
        await asyncio.sleep(2)
        # 刷新
        await page.reload()
        await asyncio.sleep(2)
        # 保存 PDF
        await page.pdf(
            path='output.pdf',
            format='A4',  # 纸张尺寸（Letter, Legal, A0-A5）
            landscape=False,  # 横向模式
            display_header_footer=True,  # 显示页眉页脚
            header_template='<div>Header</div>',
            footer_template='<div>Page <span class="pageNumber"></span></div>',
            prefer_css_page_size=True,  # 优先使用 CSS 定义的页面尺寸
            margin={'top': '1cm', 'right': '1cm', 'bottom': '1cm', 'left': '1cm'}
        )
        # 截图
        await page.screenshot(path='a.png')
        # 设置页面 HTML
        await page.set_content('<h2>Hello World</h2>')

        # 设置 User-Agent
        new_ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        # 拦截所有请求，追加 User-Agent
        await page.route("**/*", lambda route: route.continue_(
            headers={**route.request.headers, "User-Agent": new_ua}
        ))

        # 设置 Headers
        await page.set_extra_http_headers({"X-Additional-Header": "value"})
        # 关闭
        await page.close()
        await browser.close()

asyncio.run(main())
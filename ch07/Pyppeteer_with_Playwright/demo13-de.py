import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as playwright:
        # 配置浏览器绕过反爬
        browser = await playwright.chromium.launch(
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            ]
        )
        context = await browser.new_context()
        page = await context.new_page()

        try:
            # 导航并等待页面加载
            await page.goto(
                'https://spa2.scrape.center',
                wait_until="networkidle",
                timeout=90_000  # 延长导航超时
            )

            # 调试：打印页面内容
            print("页面 HTML:", await page.content())

            # 监听网络响应中的 Set-Cookie
            page.on("response", lambda response: print(
                f"Response: {response.url} - Cookies: {response.headers.get('set-cookie')}"
            ))

            # 等待任意 Cookie 出现
            await page.wait_for_function(
                "() => document.cookie.length > 0",
                timeout=60_000
            )

            # 获取并打印 Cookie
            cookies = await context.cookies()
            print("最终 Cookies:", cookies)

        except Exception as e:
            print(f"发生错误: {e}")
            await page.screenshot(path="error_debug.png")  # 错误时截图
        finally:
            await browser.close()


asyncio.run(main())
import asyncio  # Python异步IO库，用于支持异步操作
from playwright.async_api import async_playwright  # Playwright的异步API
from pyquery import PyQuery as pq  # 类似jQuery的HTML解析库

async def main():
    """
    主异步函数，用于执行网页抓取操作
    """
    # 使用async with管理Playwright上下文，确保资源正确释放
    async with async_playwright() as p:
        # 启动Chromium浏览器实例
        # headless=False表示以可视化模式运行，方便调试
        browser = await p.chromium.launch(headless=False)

        try:
            # 创建一个新页面
            page = await browser.new_page()
            # 导航到目标网址
            await page.goto('https://spa2.scrape.center')
            await page.pause()  # 进入交互式调试模式

            # 等待指定的选择器加载完成
            # .item 类名为 item 的元素
            # .name - 上述 item 元素内部类名为 name 的子元素
            await page.wait_for_selector('.item .name')
            # 获取页面HTML内容并用PyQuery解析
            html_content = await page.content()
            # 获取当前浏览器页面源代码，JS渲染之后的结果
            doc = pq(html_content)
            # 提取所有class为"item"下的"name"元素文本
            names = [item.text() for item in doc('.item .name').items()]
            print('Names:', names)
        finally:
            # 确保浏览器实例被关闭
            await browser.close()

# 运行主异步函数
if __name__ == '__main__':
    asyncio.run(main())

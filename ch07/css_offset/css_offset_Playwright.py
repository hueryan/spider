import asyncio
from playwright.async_api import async_playwright
from pyquery import PyQuery as pq
import re

PAGE_TOTAL = 503
HEADLESS = True
BASE_URL = 'https://antispider3.scrape.center/page/{page_num}'


def parse_name(name_html):
    """解析被CSS偏移混淆的姓名"""
    has_whole = name_html('.whole')
    if has_whole:
        return name_html.text()

    chars = name_html('.char')
    items = []
    for char in chars.items():
        style = char.attr('style') or ''
        match = re.search(r'left:(\d+)px', style)
        left_value = int(match.group(1)) if match else 0

        items.append({
            'text': char.text().strip(),
            'left': left_value
        })

    # 按left值从小到大排序
    items.sort(key=lambda x: x['left'])
    return ''.join(item['text'] for item in items)


async def process_page(page, page_num):
    """处理单个页面"""
    url = BASE_URL.format(page_num=page_num)
    # print(f"Processing: {url}")

    # 设置随机等待时间（降低封禁风险）
    await page.wait_for_timeout(1000)  # 1秒基础等待

    try:
        # 导航页面并等待内容加载
        await page.goto(url, wait_until='networkidle')
        await page.wait_for_selector('.item', timeout=10000)

        # 获取页面HTML内容
        html = await page.content()
        doc = pq(html)

        # 解析所有姓名
        names = doc('.item .name')
        for name_html in names.items():
            name = parse_name(name_html)
            print(f"Page {page_num}: {name}")

    except Exception as e:
        print(f"Error processing page {page_num}: {str(e)}")


async def main():
    async with async_playwright() as p:
        # 配置浏览器参数
        browser = await p.chromium.launch(
            headless=HEADLESS,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--no-sandbox',
                '--disable-setuid-sandbox'
            ]
        )

        # 创建浏览器上下文（隔离环境）
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            viewport={'width': 1920, 'height': 1080}
        )

        # 并发处理页面（控制并发数）
        semaphore = asyncio.Semaphore(10)  # 同时处理 n 个页面

        async def limited_task(page_num):
            async with semaphore:
                page = await context.new_page()
                try:
                    await process_page(page, page_num)
                finally:
                    await page.close()

        # 创建所有任务
        tasks = [limited_task(num) for num in range(1, PAGE_TOTAL + 1)]
        await asyncio.gather(*tasks)

        # 关闭资源
        await context.close()
        await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
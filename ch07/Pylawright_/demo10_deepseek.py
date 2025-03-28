from playwright.sync_api import sync_playwright
import time
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 读取本地HTML文件内容
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(current_dir, 'demo10.py')
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()


    def modify_response(route, request):
        print(f"拦截到请求: {request.url}")  # 调试输出
        route.fulfill(
            path='./demo10.html',
            status=200,
            content_type='text/html',
            # 设置 body
            body=html_content,
        )


    # 使用通配符匹配所有请求
    page.route('**/*', modify_response)

    page.goto("https://spa6.scrape.center/")
    time.sleep(8)
    browser.close()
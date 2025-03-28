from playwright.sync_api import sync_playwright

def on_response(response):
    print(f'Statue {response.status}: {response.url}')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # 监听 response事件，设置回调函数
    # 对应浏览器 Network 面板中的所有请求和相应。
    page.on('response', on_response)
    page.goto('https://spa6.scrape.center')
    page.wait_for_load_state('networkidle')
    browser.close()
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    iphone_15_pro_max = p.devices['iPhone 15 Pro Max']
    browser = p.webkit.launch(headless=False)
    context = browser.new_context(
        **iphone_15_pro_max,
        locale='zh-CN'
    )
    page = context.new_page()
    page.goto('https://www.whatismybrowser.com')
    # 等待页面的某个状态，网络空闲状态
    page.wait_for_load_state(state='networkidle')
    page.screenshot(path='browser-iphone.png')
    browser.close()
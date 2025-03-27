from playwright.sync_api import sync_playwright

# 使用已保存的状态文件跳过登录状态直接访问系统
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

    # 创建浏览器上下文时加载状态文件
    context = browser.new_context(storage_state='login_data.json')
    page = context.new_page()

    # 直接访问登录后的URL
    page.goto('https://www.csdn.net')


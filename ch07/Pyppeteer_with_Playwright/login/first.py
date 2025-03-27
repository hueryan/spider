# 首次登陆系统
from playwright.sync_api import sync_playwright
import time

with (sync_playwright() as playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.csdn.net')


    time.sleep(30)

    # 保存状态文件
    context.storage_state(path='login_data.json')
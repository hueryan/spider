from playwright.sync_api import sync_playwright
import re

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    def cancel_request(route, request):
        route.abort()
    # 通过正则传入 URL路径，这里代表所有包含 .pbg 或 .jpg 的连接，遇到后回调 cancel_request 方法处理
    # cancel_request 方法接受两参数。route 代表 CallableRoute 对象；request 代表 Request 对象。
    # 这里直接调用 CallableRoute 对象的 abort 方法，取消了这次请求，导致最终的结果是取消全部图片的加载
    page.route(re.compile(r"(\.png)|(\.jpg)"), cancel_request)
    page.goto('https://spa6.scrape.center')
    page.wait_for_load_state('networkidle')
    page.screenshot(path='no_picture.png')
    browser.close()
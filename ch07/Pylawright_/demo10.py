from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    def modify_response(route, request):
        route.fulfill(path='demo10.html')


    page.route('**/*', modify_response)
    page.goto("https://spa6.scrape.center/")
    time.sleep(8)
    browser.close()

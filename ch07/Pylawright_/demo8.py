from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://spa6.scrape.center")
    page.wait_for_load_state('networkidle')

    # 获取单个节点属性
    # 查找 class 为 name 的 a 节点， name传入 href，代表获取超链接的内容
    href = page.get_attribute('a.name', 'href')
    print(href)

    # 获取多个节点
    elements = page.query_selector_all('a.name')
    for element in elements:
        print(element.get_attribute('href'))
        # 获取节点文本
        print(element.text_content())

    # 获取单个节点
    element_one = page.query_selector('a.name')
    print(element_one.get_attribute('href'))
    print(element_one.text_content())

    browser.close()
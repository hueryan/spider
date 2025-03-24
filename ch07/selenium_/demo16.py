from selenium import webdriver
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
# 添加参数 --headless 开启无头模式
option.add_argument('--headless')
browser = webdriver.Chrome(options=option)
# 设置窗口大小
browser.set_window_size(1920, 1080)
browser.get('https://www.baidu.com')
# 页面截图
browser.get_screenshot_as_file('preview.png')
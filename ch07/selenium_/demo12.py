import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
# 开启新的选项卡
browser.execute_script("window.open()")
print(browser.window_handles)
# 切换新选项卡
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(2)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://www.python.org')
time.sleep(2)
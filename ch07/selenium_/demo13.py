from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    # 未找到报错
    browser.find_element('id', 'hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()

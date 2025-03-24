import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://antispider1.scrape.center')
time.sleep(5)
print(browser.page_source)

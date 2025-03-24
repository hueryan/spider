from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://spa2.scrape.center/'
browser.get(url)

# 获取属性值
logo = browser.find_element(By.CLASS_NAME, 'logo-image')
print(logo)
print(logo.get_attribute('src'))

# 获取文本值
input = browser.find_element(By.CLASS_NAME, 'logo-title')
print(input.text)

# 获取id、location、tag_name、size
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
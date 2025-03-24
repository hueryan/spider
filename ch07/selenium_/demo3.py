from selenium import webdriver
from selenium.webdriver.common.by import By

# 单节点
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element(By.ID, 'q')
input_second = browser.find_element(By.CSS_SELECTOR ,'#q')
input_third = browser.find_element(By.XPATH ,'//*[@id="q"]')
newline = '\n'
print(f'{input_first = }, {newline}, {input_second = }, {newline}, {input_third = }')
browser.close()


# 多节点
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
value = '.service-bd--LdDnWwA9'
lis = browser.find_elements(By.CSS_SELECTOR ,'.service-bd--LdDnWwA9 li')
# print(lis)
for li in lis:
    print(li.text)
browser.close()
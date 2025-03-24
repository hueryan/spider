from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# browser = webdriver.Chrome()
# # 隐式等待
# browser.implicitly_wait(10)
# browser.get('https://spa2.scrape.center')
# input = browser.find_element(By.CLASS_NAME, 'logo-image')
# print(input.text)
# browser.close()
# browser.quit()


browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
# 显示等待
# WebDriverWait 指定最长等待 10s.赋值给 wait
wait = WebDriverWait(browser, 10)
# 调用 until 传入等待条件
# presence_of_element_located 节点出现
# 如果节点ID为q的节点10s内加载出来，返回该节点。否则抛出异常
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)

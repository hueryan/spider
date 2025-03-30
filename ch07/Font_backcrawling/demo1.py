from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.get('https://antispider4.scrape.center')
WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item')))
html = browser.page_source
doc = pq(html)
items = doc('.item')

for item in items.items():
    name = item('.name').text()
    categories = [o.text() for o in item('.categories button').items()]
    score = item('.score').text()
    print(f'{name = } {categories = } {score = }')

browser.close()
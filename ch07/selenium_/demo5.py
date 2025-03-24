from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element(By.ID, 'draggable')
target = browser.find_element(By.ID, 'droppable') # By.CSS_SELECTOR, '#droppable' 等价
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
time.sleep(5)
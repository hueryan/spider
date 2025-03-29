from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import re

def parse_name(name_html):
    chars = name_html('.char')
    items = []
    for char in chars.items():
        items.append({
            'text':char.text().strip(),
            'left':int(re.search('(\d+)px', char.attr('style')).group(1)),
        })
        # 正则表达式的group(0)返回整个匹配的字符串;
        # group(1)则返回第一个捕获组的内容。
        # 用户的正则表达式是`(\d)px`，这里有一个捕获组，匹配的是数字，后面跟着'px'。
        # 所以，当用户调用group(0)时，会得到整个匹配的部分，比如'5px';
        # group(1)只返回数字部分，比如'5'。
        # 而groups()方法返回的是一个包含所有捕获组的元组，这里只有一个，所以返回的是('5',)。

        # print(re.search('(\d)px', char.attr('style')).group(0))
        # print(re.search('(\d)px', char.attr('style')).group(1))
        # print(re.search('(\d)px', char.attr('style')).groups())

    items = sorted(items, key=lambda x: x['left'], reverse=False)
    # print(items)
    return ''.join([item.get('text') for item in items])

options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
# browser = webdriver.Chrome()

browser.get('https://antispider3.scrape.center')
WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item')))
html = browser.page_source
doc = pq(html)
names = doc('.item .name')
for name_html in names.items():
    name = parse_name(name_html)
    print(name)
browser.close()
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

INDEX_URL = 'https://spa2.scrape.center/page/{page}'
TIME_OUT = 10
TOTAL_PAGE = 1

browser = webdriver.Chrome()
wait = WebDriverWait(browser, TIME_OUT)

# 通用爬虫方法，对任意URL进行爬取、状态监听以及异常处理
# url：爬取的URL
# condition：是页面加载成功的判断条件。可以是expected_conditions中的某一项，如 visibility_of_all_elements_located，visibility_of_elements_located等
# locator：定位器，返回元组。通过配置查询条件和参数来获取一个或者多个节点，如(By.CSS_SELECTOR, '#index .item')代表通过CSS选择器查找 #index .item 来获取列表页所有的电影信息节点。
# 在爬取过程中添加了超时检测，如到规定时间还没加载出对应的节点，抛出 TimeoutException 异常并输出错误日志
def scrape_page(url, condition, locator):
    logging.info('Scraping {}'.format(url))
    try:
        browser.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.error('error occurred while scraping %s', url, exc_info=True)

# 爬取列表页的方法，接受 page，通过调用 scrape_page 方法并传入 condition 参数和 locator 参数，完成对列表页的爬取。
# condition 传入的是 visibility_of_all_elements_located，代表所有节点都加载出来才算成功。
# 爬取页面时，不需要返回任何结果，执行完scrape_index方法后，页面处于加载完成状态，利用 browser 对象即可进行进一步的信息提取。
def scrape_index(page):
    url = INDEX_URL.format(page=page)
    # visibility_of_all_elements_located 判断条件加上CSS选择器的内容，即可判断是否加载成功
    scrape_page(url, condition=EC.visibility_of_all_elements_located,
                locator=(By.CSS_SELECTOR, '#index .item'))


from urllib.parse import urljoin
# 解析列表页
# 通过 find_elements 方法直接从列表页提取所有电影节点，接着遍历这些节点，通过get_attribute方法提取了详细页的 href 属性值，再用 urljoin 方法合成完整的URL

def parse_index():
    elements = browser.find_elements(By.CSS_SELECTOR, '#index .item .name')
    for element in elements:
        href = element.get_attribute('href')
        yield urljoin(INDEX_URL, href)

def main():
    try:
        for page in range(1, TOTAL_PAGE + 1):
            scrape_index(page)
            detail_urls = parse_index()
            logging.info('details urls %s', list(detail_urls))
    finally:
        browser.close()

if __name__ == '__main__':
    main()




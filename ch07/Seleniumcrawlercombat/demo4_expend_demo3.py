from demo3_expend_demo2 import TOTAL_PAGE, scrape_page, scrape_index, parse_index, scrape_detail, parse_detail, save_data
from selenium import webdriver
import logging

# 设置无头模式
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

def main():
    try:
        for page in range(1, TOTAL_PAGE + 1):
            scrape_index(page)
            detail_urls = parse_index()
            for detail_url in list(detail_urls):
                logging.info('get detail url %s', detail_url)
                scrape_detail(detail_url)
                detail_data = parse_detail()
                logging.info('detail data %s', detail_data)
                save_data(detail_data)
    finally:
        browser.close()

if __name__ == '__main__':
    main()
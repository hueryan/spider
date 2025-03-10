import requests
import logging
import re
from urllib.parse import urljoin
import json
from os import makedirs
from os.path import exists
import time
logging.getLogger().setLevel(logging.INFO)


BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10
RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

def scrape_page(url):
    # logging.info('Scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        # exc_info 打印出 Traceback 错误堆栈信息
        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)

def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        # print('get detail url %s', detail_url)
        # logging.info('get detail url %s', detail_url)
        yield detail_url

def scrape_detail(url):
    return scrape_page(url)

def parse_detail(html, id):
    cover_pattern = re.compile('class="ite.*?<img.*?src="(.*?)".*?class="cover">', re.S)
    name_pattern = re.compile('class="m-b-sm.*?>(.*?)</h2>', re.S)
    categories_pattern = re.compile('button.*?category.*?span>(.*?)</span>.*?</button>', re.S)
    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2}).*?上映', re.S)
    drama_pattern = re.compile('<p.*?>(.*?)</p>', re.S)
    score_pattern = re.compile('<p.*?class="score.*?>(.*?)</p>', re.S)

    cover = re.search(cover_pattern, html).group(1).strip() if re.search(cover_pattern, html) else None
    name = re.search(name_pattern, html).group(1).strip().split(':')[0] if re.search(name_pattern, html) else None
    categories = re.findall(categories_pattern, html) if re.search(categories_pattern, html) else None
    published_at = re.search(published_at_pattern, html).group(1).strip() if re.search(published_at_pattern, html) else None
    drama = re.search(drama_pattern, html).group(1).strip() if re.search(drama_pattern, html) else None
    score = re.search(score_pattern, html).group(1).strip() if re.search(score_pattern, html) else None


    return {
        'id': id,
        'cover' : cover,
        'name' : name,
        'categories' : categories,
        'published_at' : published_at,
        'drama' : drama,
        'score' : score
    }

def save_data(id, data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{id}@{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_html = scrape_index(page)
        detail_urls = parse_index(index_html)
        # logging.info("detail url %s", list(detail_urls))
        for detail_url in detail_urls:
            id = detail_url.split('/')[-1]
            detail_html = scrape_detail(detail_url)
            # print(detail_html)
            data = parse_detail(detail_html, id)

            # logging.info("get detail data %s", data)
            # print(f"get detail data %s" %data)
            # print(f'第{id}文件正在保存')
            save_data(id, data)
            # print(f'第{id}文件保存完成')





if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    run_time = end - start # 70.27691200003028 秒
    print(f'运行时间：{run_time}秒')


# [16, 51, 52, 79, 84, 85, 89, 90, 92]
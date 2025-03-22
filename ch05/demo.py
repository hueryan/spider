import requests
import logging
import pymongo
import json
from os import makedirs
from os.path import exists

RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

# mongodb 连接字符串、定义基本连接信息
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017/'
# MongoDB 数据库名
MONGO_DB_NAME = 'movies'
# MongoDB 集合名称
MONGO_COLLECTION_NAME = 'movies'

client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s : %(message)s')

INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'

TOTAL_PAGE = 10
LIMIT = 10


def scrape_api(url):
    logging.info('Scraping {}...'.format(url))
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.error(f'get invalid status code {response.status_code} while scraping {url}')
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)

def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)

DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'

def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)

def save_data_mongodb(data):
    collection.update_one({
        'name':data.get('name')
    }, {
        '$set':data
    }, upsert=True) # upsert 及时更新

def sava_data_json(id, data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{id}@{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)



def main():
    """
    :param test
    爬取第一页内容
    index_data = requests.get('https://spa1.scrape.center/api/movie/?limit=10&offset=0').json()
    print(index_data.get('results'))
    id 为 1 的网页信息
    detail_data = scrape_detail(1)
    print(detail_data)
    """
    for page in range(1, TOTAL_PAGE + 1):
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data %s', detail_data)
            save_data_mongodb(detail_data)
            logging.info('data saved successfully')
            sava_data_json(id, detail_data)


if __name__ == '__main__':
    main()
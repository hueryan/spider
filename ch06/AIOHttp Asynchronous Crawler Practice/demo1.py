import asyncio
import json
import time
import aiohttp
import logging
from motor.motor_asyncio import AsyncIOMotorClient

# 异步存储到MongoDB
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017/'
MONGO_DB_NAME = 'books'
MONGO_COLLECTION_NAME = 'demo1'

client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

INDEX_URL = 'https://spa5.scrape.center/api/book/?limit=18&offset={offset}'
DETAIL_URL = 'https://spa5.scrape.center/api/book/{id}'
PAGE_SIZE = 18
# 爬取页码数量
PAGE_NUMBER = 502
# 并发量
CONCURRENCY = 5000

# 控制最大并发量
session = None
semaphore = asyncio.Semaphore(CONCURRENCY)

async def scrape_api(url):
    async with semaphore:
        try:
            logging.info('scraping %s', url)
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError as e:
            # exc_info 打印出 Traceback 错误堆栈信息
            # logging.error('error occurred while scraping %s', url, exc_info=True)
            print('error occurred while scraping %s', url)

async def scrape_index(page):
    url = INDEX_URL.format(offset=(page - 1) * PAGE_SIZE)
    return await scrape_api(url)

async def save_data(data):
    logging.info('saving data %s', data)
    if data:
        return await collection.update_one({
            'id': data.get('id')
        }, {
            '$set': data
        }, upsert=True)
    else:
        return None

async def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    data = await scrape_api(url)
    await save_data(data)

async def main():
    global session
    session = aiohttp.ClientSession()
    try:
        scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, PAGE_NUMBER + 1)]
        results = await asyncio.gather(*scrape_index_tasks)
        logging.info('results: %s', json.dumps(results, ensure_ascii=False, indent=2))
        ids = []
        for index_data in results:
            if not index_data: continue
            for item in index_data.get('results'):
                ids.append(item['id'])
        scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]
        await asyncio.wait(scrape_detail_tasks)

    finally:
        await session.close()

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    logging.info('total time: %s', end - start)


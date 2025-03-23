import asyncio
import aiohttp

CONCURRENT_REQUESTS = 5
URL = 'https://www.baidu.com'

semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)
session = None

async def scrape_api():
    async with semaphore:
        print('scraping', URL)
        async with session.get(URL) as response:
            await asyncio.sleep(1)
            return await response.text()

async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(10)]
    await asyncio.gather(*scrape_index_tasks)

if __name__ == '__main__':
    asyncio.run(main())

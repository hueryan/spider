import asyncio
import aiohttp
from aiohttp import ClientTimeout

CONCURRENT_REQUESTS = 5
URL = 'https://www.baidu.com'
TIMEOUT_SECONDS = 10
MAX_TASKS = 10000  # 根据实际情况调整任务总量

async def scrape_api(session, semaphore):
    async with semaphore:
        try:
            print('Scraping', URL)
            timeout = ClientTimeout(total=TIMEOUT_SECONDS)
            async with session.get(URL, timeout=timeout) as response:
                # 根据实际需求决定是否需要延迟
                # await asyncio.sleep(1)
                html = await response.text()
                # 处理响应数据
                return html
        except Exception as e:
            print(f"Request failed: {str(e)}")
            return None

async def main():
    semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(scrape_api(session, semaphore))
            for _ in range(MAX_TASKS)
        ]
        # 批量等待任务完成并处理结果
        results = await asyncio.gather(*tasks)
        # 可在此处处理所有结果，例如保存到文件或数据库
        # 示例：统计成功请求数
        success_count = sum(1 for res in results if res is not None)
        print(f"Successfully completed {success_count}/{MAX_TASKS} requests")

if __name__ == '__main__':
    asyncio.run(main())
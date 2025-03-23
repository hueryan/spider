import asyncio
import requests
import time

start = time.time()

async def get(url): #  每个请求页面方法独立出来，用async修饰，得到一个协程对象
    return requests.get(url)

async def request_with_await():
    url = 'https://www.httpbin.org/delay/5'
    print('Waiting for', url)
    response =await get(url)
    print('Get response from', url, 'response', response)

tasks = [asyncio.ensure_future(request_with_await()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)
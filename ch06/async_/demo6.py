import asyncio
import requests
import time

start = time.time()

async def request_without_await():
    url = 'https://www.httpbin.org/delay/5'
    print('Waiting for', url)
    response = requests.get(url)
    print('Get response from', url, 'response', response)

tasks = [asyncio.ensure_future(request_without_await()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print('Cost time:', end - start)
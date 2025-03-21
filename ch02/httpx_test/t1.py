import requests
# https://www.python-httpx.org/
import httpx

# 通过 auth 传入账号密码进行验证
# url = "https://ssr3.scrape.center/"
# response = requests.get(url, auth=('admin', 'admin'))
# print(response.status_code)

url = 'https://spa16.scrape.center'
# response = requests.get(url)
# 开启协议 http2
# client = httpx.Client(http2=True)
# response = client.get(url)
# # print(response.text)

# with httpx.Client(http2=True) as client:
#     response = client.get(url)
#     print(response.status_code)

# # Client
# headers = {'User-Agent':'my-app/0.0.1'}
# with httpx.Client(headers=headers, http2=True) as client:
#     response = client.get('https://www.httpbin.org/get')
#     print(response.json()['headers']['User-Agent'])
#     print(response.http_version)

import asyncio
async def fetch(url):
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get(url)
        print(response.text)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(fetch('https://www.httpbin.org/get'))
import aiohttp
import asyncio

async def main():
    data = {'name':'germey', 'age':25}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://www.httpbin.org/post', json=data) as response:
            print('status:', response.status)
            print('headers:', response.headers)
            print('body:', await response.text())
            print('bytes:', await response.read())
            print('json:', await response.json())


if __name__ == '__main__':
    asyncio.run(main())


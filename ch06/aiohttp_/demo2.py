import aiohttp
import asyncio

async def main():
    params = {'name':'germey', 'age':25}
    async with aiohttp.ClientSession() as session:
        # async with session.get('https://www.httpbin.org/get', params=params) as response:
        # async with session.post('https://www.httpbin.org/post', data=b'data') as response:
        # async with session.put('https://www.httpbin.org/put', data=b'data') as response:
        # async with session.delete('https://www.httpbin.org/delete') as response:
        # async with session.head('https://www.httpbin.org/get') as response:
        # async with session.options('https://www.httpbin.org/get') as response:
        async with session.patch('https://www.httpbin.org/patch', data=b'data') as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.run(main())
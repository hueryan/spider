from typing import Tuple, Any

import aiohttp
# 导入协程库
import asyncio
import typing

async def fetch(session, url) -> tuple[Any, Any]:
    async with session.get(url) as response:
        return await response.text(), response.status

async def main() -> None:
    async with aiohttp.ClientSession() as session:
        html, status = await fetch(session, 'https://www.cuiqingcai.com')
        print(f'html: {html[:100]}...')
        print(f'status: {status}')

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # run 代替最后的启动操作，不用声明事件循环，其内部会自动启动一个事件循环
    asyncio.run(main())
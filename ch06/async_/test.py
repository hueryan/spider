import asyncio
import time


async def print_even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            print(f'Even number: {i}')
            await asyncio.sleep(1)  # 让出控制权给事件循环

async def print_odd_numbers(n):
    for i in range(n):
        if i % 2 != 0:
            print(f'Odd number: {i}')
            await asyncio.sleep(1)  # 让出控制权给事件循环

async def main():
    n = 10
    # # 使用asyncio.gather并发执行两个协程
    # await asyncio.gather(
    #     print_odd_numbers(n),
    #     print_even_numbers(n)
    # )
    results = asyncio.as_completed([print_even_numbers(10),
                                   print_odd_numbers(n)])
    for result in results:
        await result

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
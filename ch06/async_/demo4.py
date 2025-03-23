import asyncio
import requests

async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

def callback(task):
    if task.cancelled():
        print("任务被取消")
    elif task.exception():
        print(f"发生异常：{task.exception()}")
    else:
        print(f"Status：{task.result()}")

coroutine = request()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)

# 不用19行添加回调函数也可以得到结果
# print('Task Result:', task.result())
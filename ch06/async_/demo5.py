import asyncio
import requests  # 导入同步HTTP请求库

# 定义异步函数（注意：内部使用同步操作会阻塞事件循环）
async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)  # 同步阻塞操作，实际会破坏异步特性
    return status  # 返回requests的Response对象

# 创建包含5个相同协程的任务列表
tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('Tasks:', tasks)  # 打印所有任务对象（此时均为pending状态）

# 获取事件循环管理器
loop = asyncio.get_event_loop()
# 运行事件循环直到所有任务完成（实际会顺序执行而非并发）
loop.run_until_complete(asyncio.wait(tasks))  # asyncio.wait用于等待多个任务

# 遍历已完成的任务
for task in tasks:
    # 打印每个任务的返回结果（Response对象）
    print('Task Result:', task.result())  # 需要.status获取状态码
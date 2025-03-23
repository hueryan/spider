import asyncio  # 导入异步IO库

# 定义一个异步函数（协程函数）
async def execute(x):
    print('Number:', x)  # 当协程被执行时，打印参数x的值

# 调用异步函数不会直接执行，而是返回一个协程对象
coroutine = execute(1)
# 此时协程尚未执行，打印结果类似：Coroutine: <coroutine object execute at 0x...>
print('Coroutine:', coroutine)
print('After calling execute')  # 这里会立即输出，因为协程还没开始运行

# 获取事件循环（管理异步任务的"调度器"）
loop = asyncio.get_event_loop()
# 将协程交给事件循环并启动，此时会真正执行print('Number:', 1)
loop.run_until_complete(coroutine)
print('After calling loop')  # 协程执行完毕后才输出这行
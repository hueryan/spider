import asyncio  # 导入异步IO库

# 定义异步函数
async def execute(x):
    print('Number:', x)  # 当协程被执行时，打印参数x的值
    return x  # 返回参数x作为协程结果

# 调用异步函数得到协程对象（尚未执行）
coroutine = execute(1)
print('Coroutine:', coroutine)  # 打印协程对象内存地址
print('After calling execute')  # 立即输出，协程仍未执行

# 获取事件循环（异步任务调度器）
loop = asyncio.get_event_loop()

# 两种创建任务的方式（实际重复创建了，后者会覆盖前者）
# task = loop.create_task(coroutine)  # 方式1：通过loop创建任务
task = asyncio.ensure_future(coroutine)  # 方式2：通用方法创建任务（效果相同）

print('Task: ', task)  # 查看任务状态（此时状态为 pending）
loop.run_until_complete(task)  # 运行事件循环直到任务完成
print('Task: ', task)  # 查看任务状态（此时状态为 finished，含结果）
print('After calling loop')  # 整个异步流程结束后输出
# 未处理任务结果
print(task.result())
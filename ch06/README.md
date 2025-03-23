# 异步爬虫

## Async

| 阻塞       | 非阻塞   |
| ---------- | -------- |
| **同步**   | **异步** |
| **多进程** | **协程** |

### 协程

- event_loop：事件循环



### Py程序

- demo1：delay3，for 10 用时44.8325s
- demo2：简单协程
- demo3：task
  - `loop.create_task()` 和 `asyncio.ensure_future()` 效果等价
  - 任务对象会经历 pending -> running -> finished 状态变化
  - 协程结果存储在 `task.result()` 中（需在任务完成后获取）
  - 异步代码直到 `run_until_complete()` 才会真正执行
- demo4：绑定回调
- demo5：多任务协程
- demo6：协程实现 
- demo7： 引入await。
- demo8：实现真正协程

`pip install aiohttp` [_](https://setup.scrape.center/aiohttp) 

[aiohttp 官方文档](http://aiohttp.readthedocs.io/en/stable) 

字符编码检测库 cchardet，加速 DNS 解析库 aiodns

- demo9：测试百度


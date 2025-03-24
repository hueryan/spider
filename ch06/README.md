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

## aiohttp

- demo1：需要引入asyncio，启动协程。
  - 每个方法添加 `async` 
  - 返回协程对象的前加 `await` 
- demo2：get请求
  - post
  - put
  - delete
  - head
  - options
  - patch
- demo3：post from、JSON
  - data只能是str或者dict。传json数据时将请求头中 `Content-Type` 改为 `application/json` 。只需要将post方法中data参数改为json
- demo4：timeout 更多参考[aiohttp](https://docs.aiohttp.org/en/stable/client_quickstart.html#timeouts) 
- demo5：控制并发量

## multiprocessing

参考 [官方文档](https://docs.python.org/zh-cn/3/library/multiprocessing.html) 

**demo14.py：**

- 使用 aiohttp 框架搭建了一个简单的 Web 服务器。
- 定义了一个根路径处理函数，在接收到请求后会延迟3秒，然后返回文本 "Hi"。
- 服务器运行在5000端口。

**demo15.py：**

- 用来测试对 demo14.py 启动的服务器进行请求的性能。
- 提供了三种请求方式：
  - **循环方式**：利用 requests 库同步逐个请求。
  - **线程池方式**：利用 ThreadPoolExecutor 实现多线程并发请求。
  - **异步方式**：利用 aiohttp 库的异步请求来并发发起请求。
- 最后使用 timeit 模块测量各方式的执行时间，从而比较它们的性能。

## 实战

`pip install motor` [_](https://setup.scrape.center/motor) 

- demo1：爬取 spa5 网站
- demo2：类。。。

import requests  # 用于发送HTTP请求
import time     # 用于计算执行时间
import multiprocessing  # 用于创建多进程实现并发



# 定义发送请求的函数，参数'_'表示忽略传入的参数（常规做法）
def request(_):
    url = 'https://ssr4.scrape.center/'
    print('Waiting for', url)
    try:
        # 发送GET请求并获取响应文本
        result = requests.get(url).text
        # 打印结果（注意：响应内容过长时可能影响可读性）
        print('Get response from', url, 'Result length:', len(result))
    except Exception as e:
        # 异常处理，防止单个进程崩溃影响整体
        print('Error occurred:', str(e))

if __name__ == '__main__':
    # 获取当前系统的CPU核心数量
    cpu_count = multiprocessing.cpu_count()
    print('CPU count:', cpu_count)

    # 记录脚本开始执行的时间
    start = time.time()
    # 创建进程池，进程数设置为CPU核心数（通常为最优并发数）
    pool = multiprocessing.Pool(cpu_count)

    # 使用进程池的map方法分配任务
    # 问题：参数列表[1]仅包含一个元素，实际只创建一个任务，未能利用多核优势
    # 使用range(n)生成多个任务，以充分测试并发
    pool.map(request, range(100))

    # 等待所有进程执行完毕（map方法本身是阻塞的，此处可省略join）
    pool.close()
    pool.join()

    # 记录脚本结束时间并计算总耗时
    end = time.time()
    print('Total time cost:', end - start)
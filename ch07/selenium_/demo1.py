# 导入Selenium相关模块
from selenium import webdriver  # 浏览器驱动
from selenium.webdriver.common.keys import Keys  # 键盘按键模拟
from selenium.webdriver.support.ui import WebDriverWait  # 显式等待
from selenium.webdriver.support import expected_conditions as EC  # 等待条件
from selenium.webdriver.common.by import By  # 元素定位方式

# 创建Chrome浏览器实例（注意变量名拼写应为browser）
browser = webdriver.Chrome()  # 自动打开Chrome浏览器窗口

try:
    # 访问百度首页
    browser.get('https://www.baidu.com')  # 浏览器加载指定URL

    # 定位搜索输入框（通过id选择器）
    input = browser.find_element(By.ID, 'kw')  # 找到百度搜索输入框

    # 输入搜索关键词并回车
    input.send_keys('Python')  # 输入文本"Python"
    input.send_keys(Keys.ENTER)  # 模拟键盘回车操作

    # 显式等待：直到搜索结果区域加载完成（最多等待10秒）
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))  # 等待搜索结果区域出现 通过id查询 content_left

    # 输出页面信息
    print(browser.current_url)  # 打印当前页面URL
    print(browser.get_cookies())  # 获取并打印当前页面Cookies
    print(browser.page_source)  # 获取并打印网页源代码（HTML内容）

finally:
    # 确保无论是否发生异常都会关闭浏览器
    browser.close()  # 关闭浏览器窗口（释放资源）
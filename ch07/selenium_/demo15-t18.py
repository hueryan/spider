# 导入Selenium的WebDriver模块和Chrome浏览器配置选项
from selenium import webdriver
from selenium.webdriver import ChromeOptions

# 创建Chrome浏览器配置选项对象
option = ChromeOptions()

# 通过实验性选项排除"enable-automation"启动参数（防止被检测为自动化工具）
# ChromeDriver 79+版本后，默认启用自动化控制标志，此设置可以隐藏自动化特征
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 禁用Chrome的自动化扩展程序（进一步防止被识别为自动化浏览器）
option.add_experimental_option('useAutomationExtension', False)

# 创建带有自定义配置的Chrome浏览器实例
browser = webdriver.Chrome(options=option)

# 执行JavaScript脚本，删除navigator.webdriver属性（绕过反爬虫检测的关键步骤）
# 标准浏览器中navigator.webdriver属性为undefined，自动化工具会暴露为true
browser.execute_script('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')

# 访问目标网站（这是一个用于测试反爬虫技术的演示网站）
browser.get('https://antispider1.scrape.center')
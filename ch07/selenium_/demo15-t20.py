# 导入Selenium核心模块和Chrome浏览器配置项
from selenium import webdriver
from selenium.webdriver import ChromeOptions

# 创建Chrome浏览器配置对象
option = ChromeOptions()

# 关键反检测配置1：禁用自动化控制标识
# 移除ChromeDriver的"enable-automation"启动参数（消除顶部自动化提示栏）
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 关键反检测配置2：阻止加载自动化扩展
# 禁用ChromeDriver自带的自动化扩展程序（避免生成相关浏览器扩展）
option.add_experimental_option('useAutomationExtension', False)

# 可添加的额外配置示例
option.add_argument('--disable-blink-features=AutomationControlled')  # 禁用自动化控制特征
option.add_argument('--disable-gpu')  # 部分反爬系统会检测GPU渲染特征

# 实例化经过反检测配置的浏览器对象
# 注意：需要确保本地Chromedriver版本与Chrome浏览器版本匹配
browser = webdriver.Chrome(options=option)

# 高级反检测技术：通过Chrome开发者工具协议(CDP)注入脚本
# 使用Page.addScriptToEvaluateOnNewDocument方法：
# 1. 在浏览器创建新文档时立即执行（早于页面资源加载）
# 2. 永久修改navigator对象的webdriver属性（直到浏览器进程结束）
# 3. 比传统execute_script方法更早生效，有效规避检测
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': '''
    Object.defineProperty(navigator, "webdriver", {
        get: () => undefined  // 重写属性获取器，始终返回undefined
    })'''
})

# 访问反爬虫测试站点（崔庆才的爬虫教学示例站点）
# 该站点专门用于演示常见反爬虫技术，测试绕过效果
browser.get('https://antispider1.scrape.cuiqingcai.com/')
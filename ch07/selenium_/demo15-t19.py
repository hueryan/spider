# 导入Selenium核心模块和Chrome浏览器配置项
from selenium import webdriver
from selenium.webdriver import ChromeOptions

# 创建Chrome浏览器配置对象
option = ChromeOptions()

# 关键反检测配置1：移除"enable-automation"启动参数
# 防止浏览器顶部显示"Chrome正受到自动测试软件的控制"提示
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 关键反检测配置2：禁用自动化扩展组件
# 避免加载ChromeDriver自带的自动化扩展程序（默认加载的）
option.add_experimental_option('useAutomationExtension', False)

# 实例化经过配置的Chrome浏览器对象
browser = webdriver.Chrome(options=option)

# 核心改进点：使用Chrome DevTools Protocol(CDP)注入脚本
# 通过Page.addScriptToEvaluateOnNewDocument命令：
# 1. 在浏览器创建新文档时自动执行脚本（早于页面加载）
# 2. 比直接execute_script更早修改环境变量，避免检测
# 3. 永久删除navigator.webdriver属性（直到浏览器关闭）
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': '''
    Object.defineProperty(navigator, "webdriver", {
        get: () => undefined
    })'''
})

# 访问目标测试页面（反爬虫演示站点）
browser.get('https://antispider1.scrape.center')
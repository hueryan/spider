import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        '''
            为两个用户进行存储
            context1 = await p.chromium.launch_persistent_context(user_data_dir='./user1_data')
            context2 = await p.chromium.launch_persistent_context(user_data_dir='./user2_data')
        '''
        # 直接创建持久化上下文（包含浏览器实例）
        context = await p.chromium.launch_persistent_context(
            user_data_dir='./userdata',  # 用户数据目录
            headless=False,
            ignore_default_args = ['--enable-automation'],  # 隐藏Chrome提示栏
            # 可选反检测配置
            viewport={'width': 1280, 'height': 720},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
        )

        # 使用持久化上下文创建页面
        page = await context.new_page()
        await page.add_init_script('''
            Object.defineProperty(navigator, "webdriver", {
            get:()=> undefined
            });
        ''')
        # 访问页面
        # await page.goto('https://www.taobao.com')
        await page.goto('https://www.csdn.net')

        # 模拟登录操作（假设需要手动操作）
        # 此处可能需要处理登录验证码或其他反爬机制
        await asyncio.sleep(30)


asyncio.run(main())
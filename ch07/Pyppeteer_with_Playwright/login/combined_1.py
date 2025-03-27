from playwright.sync_api import sync_playwright
import os
import time

def main():
    with sync_playwright() as playwright:
        # 启动浏览器
        browser = playwright.chromium.launch(headless=False)

        # 判断是否存在登录状态文件
        if os.path.exists('login_data.json'):
            try:
                # 尝试使用已有登录状态
                context = browser.new_context(storage_state='login_data.json')
                page = context.new_page()
                page.goto('https://www.csdn.net')

                # 验证登录状态是否有效（根据页面元素判断）
                if page.query_selector('.user-info'):  # 根据实际登录后的元素调整
                    print("成功复用登录状态")
                    time.sleep(10)  # 保持页面打开观察
                    return
                else:
                    print("登录状态已过期")
                    context.close()
                    os.remove('login_data.json')  # 删除无效状态文件
            except:
                print("状态文件加载失败")
                os.remove('login_data.json')

        # 需要新登录流程
        print("开始首次登录流程...")
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://www.csdn.net')

        # 等待手动登录（可根据需要添加自动登录代码）
        print("请手动完成登录操作（30秒）...")
        time.sleep(30)



        # # 自动登录示例（需根据实际页面元素调整）
        # page.fill('#username', 'your_username')
        # page.fill('#password', 'your_password')
        # page.click('#login-button')
        # page.wait_for_selector('.user-info')  # 等待登录成功元素


        # 验证登录是否成功
        if page.query_selector('.user-info'):  # 根据实际登录后的元素调整
            # 保存有效的登录状态
            context.storage_state(path='login_data.json')
            print("登录状态已保存")
        else:
            print("登录未完成或失败")

        time.sleep(5)  # 最终观察时间
        context.close()


if __name__ == "__main__":
    main()
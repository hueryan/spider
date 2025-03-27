from playwright.sync_api import sync_playwright
import os
import time
import argparse  # 新增参数解析模块


def main():
    # ==================== 命令行参数解析 ====================
    parser = argparse.ArgumentParser(description='CSDN自动登录脚本')
    parser.add_argument('--force-login',
                        action='store_true',
                        help='强制重新登录（即使存在登录状态文件）')
    args = parser.parse_args()

    parser.add_argument('--timeout',
                        type=int,
                        default=30,
                        help='手动登录等待时间（秒）')

    with sync_playwright() as playwright:
        # ==================== 浏览器初始化 ====================
        browser = playwright.chromium.launch(headless=False)

        # ==================== 登录状态管理逻辑 ====================
        # 如果强制登录参数被指定 且 存在旧状态文件 -> 清理旧状态
        if args.force_login and os.path.exists('login_data.json'):
            try:
                os.remove('login_data.json')
                print("已清除旧登录状态文件")
            except Exception as e:
                print(f"删除状态文件失败: {str(e)}")

        # 状态文件存在 且 未强制登录 -> 尝试复用
        if not args.force_login and os.path.exists('login_data.json'):
            try:
                # ==================== 复用登录状态 ====================
                context = browser.new_context(storage_state='login_data.json')
                page = context.new_page()
                page.goto('https://www.csdn.net')

                # 通过用户信息元素验证登录状态
                if page.query_selector('.user-info'):  # 根据实际页面元素调整
                    print("✅ 登录状态复用成功")
                    time.sleep(10)
                    return
                else:
                    print("❌ 登录状态已过期")
                    context.close()
                    os.remove('login_data.json')
            except Exception as e:
                print(f"❌ 状态加载失败: {str(e)}")
                if os.path.exists('login_data.json'):
                    os.remove('login_data.json')

        # ==================== 新登录流程 ====================
        print("🚀 开始新登录流程...")
        context = browser.new_context()
        page = context.new_page()

        # 访问登录页面
        page.goto('https://passport.csdn.net/login')
        print("⏳ 请手动完成登录操作（30秒）...")

        # 登录等待（实际项目建议使用 wait_for_selector 替代 sleep）
        time.sleep(30)

        # 登录后验证
        if page.query_selector('.user-info'):  # 根据实际页面元素调整
            # 保存有效的登录状态
            context.storage_state(path='login_data.json')
            print("✅ 登录状态已保存")
            time.sleep(5)
        else:
            print("❌ 登录未完成或失败")

        context.close()


if __name__ == "__main__":
    main()
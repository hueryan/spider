"""
CSDN自动化登录脚本
作者：智能助手
版本：2.1
功能：支持多账号管理、自定义超时时间和状态文件路径
更新日期：2023-10-05
"""

from playwright.sync_api import sync_playwright
import os
import time
import argparse

def main():
    # ==================== 命令行参数解析 ====================
    parser = argparse.ArgumentParser(
        description='CSDN自动化登录脚本 - 支持多账号和自定义配置',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-u', '--username',
                       default=None,
                       help='指定登录账号（用于多账号管理）')
    parser.add_argument('--state-file',
                       help='登录状态存储路径（优先级高于--username参数）')
    parser.add_argument('--timeout',
                       type=int,
                       default=30,
                       help='手动登录等待时间（单位：秒）')
    parser.add_argument('--force-login',
                       action='store_true',
                       help='强制重新登录（忽略现有状态文件）')
    args = parser.parse_args()

    # ==================== 状态文件路径计算 ====================
    if args.state_file:
        state_path = os.path.abspath(args.state_file)
    elif args.username:
        state_path = os.path.abspath(f'login_data_{args.username}.json')
    else:
        state_path = os.path.abspath('login_data.json')

    # ==================== 浏览器初始化 ====================
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        # ==================== 强制登录处理 ====================
        if args.force_login and os.path.exists(state_path):
            try:
                os.remove(state_path)
                print(f"🗑️ 已强制删除旧状态文件：{state_path}")
            except Exception as e:
                print(f"❌ 文件删除失败：{str(e)}")
                return

        # ==================== 登录状态复用尝试 ====================
        if not args.force_login and os.path.exists(state_path):
            try:
                context = browser.new_context(storage_state=state_path)
                page = context.new_page()
                page.goto('https://www.csdn.net')

                # 根据用户信息元素验证登录状态
                if page.query_selector('.user-info'):  # ⚠️请根据实际页面元素调整
                    print(f"✅ 登录状态复用成功：{state_path}")
                    print("🔍 检测到有效用户信息，正在保持会话...")
                    time.sleep(10)
                    return
                else:
                    print("⚠️ 登录凭证已过期")
                    context.close()
                    os.remove(state_path)
            except Exception as e:
                print(f"❌ 状态加载失败：{str(e)}")
                if os.path.exists(state_path):
                    os.remove(state_path)

        # ==================== 新登录流程 ====================
        print(f"🚀 开始登录流程，状态文件将保存至：{state_path}")
        context = browser.new_context()
        page = context.new_page()

        # 访问登录页面
        page.goto('https://passport.csdn.net/login')
        print(f"⏳ 请在 {args.timeout} 秒内完成登录操作...")
        print("👉 操作提示：")
        print("1. 输入账号密码")
        print("2. 完成人机验证（如有）")
        print("3. 等待页面自动跳转")

        # 登录等待
        time.sleep(args.timeout)

        # 登录后验证
        if page.query_selector('.user-info'):  # ⚠️请根据实际页面元素调整
            # 保存有效的登录状态
            context.storage_state(path=state_path)
            print(f"💾 登录状态已保存至：{state_path}")
            print("🕒 5秒后自动关闭...")
            time.sleep(5)
        else:
            print("❌ 登录失败可能原因：")
            print("- 超时未完成登录")
            print("- 验证失败")
            print("- 网络连接问题")

        context.close()

if __name__ == "__main__":
    print("="*50)
    print("CSDN自动化登录工具")
    print("功能说明：")
    print("- 自动保存/复用登录状态")
    print("- 支持多账号管理")
    print("- 支持强制重新登录")
    print("="*50)
    main()
# combined_2-v1

1. 常规使用（复用登录状态）

```bash
python combined_2-v1.py
```

2. 强制重新登录

```shell
python combined_2-v1.py --force-login
```

3. 获取帮助信息

```shell
python combined_2-v1.py --help
```

```
usage: combined_2-v1.py [-h] [--force-login]

CSDN自动登录脚本

optional arguments:
  -h, --help    show this help message and exit
  --force-login 强制重新登录（即使存在登录状态文件）
```





# combined_2-v2

1. **多账号支持**

   ```
   # 用户1登录
   python combined_2-v2.py.py -u user1
   # 用户2登录
   python combined_2-v2.py.py -u user2
   ```

   - 自动生成独立状态文件：`login_data_user1.json`、`login_data_user2.json`

2. **自定义状态文件路径**

   ```
   python combined_2-v2.py.py --state-file /custom/path/my_state.json
   ```

3. **灵活超时控制**

   ```
   # 设置45秒操作时间
   python combined_2-v2.py.py --timeout 45
   ```

4. **强制重新登录**

   ```
   python combined_2-v2.py.py --force-login
   ```

### 使用示例

场景1：多账号管理

```
# 首次登录用户A
python combined_2-v2.py -u userA
# 复用用户A的登录状态
python combined_2-v2.py -u userA

# 切换用户B登录
python combined_2-v2.py -u userB
```

场景2：自定义配置

```
# 指定存储路径和超时时间
python combined_2-v2.py --state-file ~/csdn_states/admin.json --timeout 45
```

场景3：强制刷新登录

```
# 忽略现有状态强制重新登录
python combined_2-v2.py -u userA --force-login
```
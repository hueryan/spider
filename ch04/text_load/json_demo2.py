import json
# 读取方式
with open('str.json', encoding='utf-8') as f:
    # 通过read获取再转化
    str = f.read()
    data = json.loads(str)
    print(data)

# load 加载文件
data = json.load(open('str.json', encoding='utf-8'))
print(data)
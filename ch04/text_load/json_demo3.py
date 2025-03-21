import json

data = [{
    'name':'Bob',
    'gender':'male',
    'birthday':'1992-10-18',
}]
print('open(w)-9 line', '='*50)
with open('data_9.json', 'w', encoding='utf-8') as f:
    # 将 JSON 对象转化成 str
    # f.write(json.dumps(data))
    f.write(json.dumps(data, indent=2))



# 中文
data = [{
    'name':'王伟',
    'gender':'男',
    'birthday':'1992-10-18',
}]

# 写入方式
print('open(w)-25 line', '='*50)
with open('data_25.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=2))

print('open(w)-29 line', '='*50)
with open('data_29.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=2, ensure_ascii=False))

print('open(w)-34 line', '='*50)
# 第一个参数为 JSON 对象，第二个参数可以传入文件操作对象
json.dump(data, open('data_34.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
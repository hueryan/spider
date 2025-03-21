import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''


# print(str)
# print(type(str))
data = json.loads(str)
# print(data)
# print(type(data))
print(data[0]['name'])
print(type(data[0]))
# get 通过获取key获取value
print(data[0].get('name'))
# get获取时当key不存在是，返回None.当含有第二个参数时打印第二个
print(data[0].get('age'))
print(data[0].get('age', 25))

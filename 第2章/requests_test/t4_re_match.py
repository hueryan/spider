import re

content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# match
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())
# print(result.span())

# 匹配目标
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld', content)
# print(result.group(1))

# 通用匹配
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$', content)
# print(result)

# # 贪婪
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*(\d+).*Demo$', content)
# print(result.group(1))
#
# # 非贪婪
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$', content)
# print(result.group(1))

# 中间尽量用非贪婪，结尾尽量用贪婪
# content = 'https://weibo.com/comment/kEraCN'
# result1 = re.match('http.*comment/(.*?)', content)
# result2 = re.match('http.*comment/(.*)', content)
# print("result1: ", result1.group(1))
# print("result2: ", result2.group(1))
# print(result1, result2)

# 修饰符
content = """Hello 1234567 World_This 
is a Regex Demo
"""
result = re.match('He.*?(\d+).*?Demo$', content, re.S)
# print(result.group(1))

# 转义匹配
content = "(百度) www.baidu.com"
result = re.match('\(百度\).www\.baidu\.com$', content)
result = re.match('\(百度\).*?com$', content)
print(result)
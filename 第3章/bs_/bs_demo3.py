from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

soup = BeautifulSoup(html, 'lxml')
# 输出标签
print(soup.title)
print(type(soup.title))
# 输出标签文本
print(soup.title.string)
print(soup.head)
# 只选择第一个其他忽略
print(soup.p)
# name属性 获取节点名称
print(soup.title.name)

# attrs 获取属性、属性值
print(soup.p.attrs)
# name 有一个 返回str，class可能有多个 返回list
print(soup.p.attrs['name'])
print(soup.p['class'])

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
"""

soup = BeautifulSoup(html, 'lxml')
# 嵌套调用
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)
from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
# 获取p节点的所有直接孩子节点 contents
# print(soup.p.contents)
for i, content in enumerate(soup.p.contents):
    print(i, content)

# child 获取p的孩子节点生成器
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)

# 获取所有p的子孙节点 descendants
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)




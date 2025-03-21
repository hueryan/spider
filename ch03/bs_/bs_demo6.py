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
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
# 获取直接父节点
print(soup.a.parent)

html = """
<html>
    <body>
        <p class="story">
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
        </p>
"""
soup = BeautifulSoup(html, 'lxml')

print(type(soup.a.parents))
# 所有祖先节点
print(list(enumerate(soup.a.parents)))

html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
"""

soup = BeautifulSoup(html, 'lxml')

# 获取兄弟节点
print("Next Sibling", soup.a.next_sibling)
print("Prev Sibling", soup.a.previous_sibling)
print('Next Siblings', list(enumerate(soup.a.next_siblings)))
print("Prev Siblings", list(enumerate(soup.a.previous_siblings)))

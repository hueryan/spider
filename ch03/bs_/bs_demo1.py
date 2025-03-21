from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello</p>', 'lxml')
# soup.标签.string 获取该标签文本
print(soup.p.string)
from bs4 import BeautifulSoup

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
# 通过 name 查询ul标签
print('通过 name 查询ul标签', '第24行', '*'*30)
print(soup.find_all('ul'))
print(type(soup.find_all('ul')[0]))

for ul in soup.find_all('ul'):
    print(ul.find_all('li'))

# 查 ul -> li.string
for ul in soup.find_all('ul'):
    print(ul.find_all('li'))
    for li in ul.find_all('li'):
        print(li.string)

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
# 通过 attrs 查询节点
print('通过 attrs 查询节点', '第58行', '*'*30)
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))
print('直接写属性查询节点', '第61行', '*'*30, 'id、class_')
# 直接通过(id、class_)等查询
print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))




# 通过 text 查询
print('通过 text 查询第67行', '*'*30)
import re
html='''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(string=re.compile('link')))

# find查找
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.find(name='ul'))
print(type(soup.find(name='ul')))
print(soup.find(class_='list'))
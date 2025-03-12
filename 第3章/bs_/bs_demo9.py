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
# select css选择器
# 选择class为panel下 panel-heading 的标签
print(soup.select('.panel .panel-heading'))
# 选择所有 ul 下 li 标签
print(soup.select('ul li'))
# 选择 id 下class为element的标签
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))

# 嵌套选择、获取所有 ul 标签下li对象
for ul in soup.select('ul'):
    print(ul.select('li'))

# 获取属性
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

# 获取节点文本值
for li in soup.select('li'):
    print('Get text: ', li.get_text())
    print('String: ', li.string)
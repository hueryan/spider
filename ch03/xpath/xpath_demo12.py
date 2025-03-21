from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>
'''
html = etree.HTML(text)

# 获取所有祖先节点
results = html.xpath('//li[1]/ancestor::*')
print(len(results), '    ancestor::*')
for result in results:
    print(etree.tostring(result).decode('utf-8'))

# 获取所有标签为 div 的父节点
results = html.xpath('//li[1]/ancestor::div')
print(len(results),'    ancestor::div')
for result in results:
    print(etree.tostring(result).decode('utf-8'))

# 获取所有标签 li 的所有属性值
results = html.xpath('//li/attribute::*')
print(len(results),'    attribute::*')
print(results)

# 获取第一个标签 li 直接孩子属性为@href="link1.html"的  a 标签
results = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(len(results),'    child::a[@href="link1.html"]')
for result in results:
    print(etree.tostring(result).decode('utf-8'))

# 获取第一个标签 li 所有子孙节点为 span 的标签
results = html.xpath('//li[1]/descendant::span')
print(len(results),'    descendant::span')
for result in results:
    print(etree.tostring(result).decode('utf-8'))

# 获取当前节点之后的所有节点 选择第二个
results = html.xpath('//li[1]/following::*[2]')
print(len(results),'    following::*[2]')
for result in results:
    print(etree.tostring(result).decode('utf-8'))

# 获取该节点的所有兄弟节点
results = html.xpath('//li[1]/following-sibling::*')
print(len(results),'    following-sibling::*')
for result in results:
    print(etree.tostring(result).decode('utf-8'))
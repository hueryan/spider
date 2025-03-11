from lxml import etree

text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)

# 获取多属性值（可以筛除一部分标签文本）
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(result)
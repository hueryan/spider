from lxml import etree

text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''

html = etree.HTML(text)
# 无法获取结果
result = html.xpath('//li[@class="li"]')
print(result)

# contains 可以获取属性多值
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)
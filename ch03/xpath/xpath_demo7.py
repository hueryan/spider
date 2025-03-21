from lxml import etree

html = etree.parse('xpath_test.html', etree.HTMLParser())
# / 获取的是li的直接子节点，结果是 a 标签
result = html.xpath('//li[@class="item-0"]/text()')
print(result)

# // 获取的是li的子孙节点的text()
result =  html.xpath('//li[@class="item-0"]//text()')
print(result)

# 通过获取 a 标签在获取文本
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)
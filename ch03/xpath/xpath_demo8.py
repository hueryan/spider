from lxml import etree

html = etree.parse('xpath_test.html', etree.HTMLParser())
# 通过@获取a的属性值
result = html.xpath('//li/a/@href')
print(result)
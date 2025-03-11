from lxml import etree

html = etree.parse('xpath_test.html', etree.HTMLParser())
# 通过@获取对应标签
results = html.xpath('//li[@class="item-0"]')
for result in results:
    print(etree.tostring(result).decode('utf-8').replace('&#13',''))
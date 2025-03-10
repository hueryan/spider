from lxml import etree

html = etree.parse('xpath_test.html', etree.HTMLParser())
# 获取所有父节点为 li 的 a 标签
# / 用于获取结点的直接子节点
results_li_a = html.xpath('//li/a')
for result in results_li_a:
    print(etree.tostring(result).decode('utf-8').replace('&#13',''))


# // 用于获取结点的子节点
results_ul__a = html.xpath('//ul//a')
for result in results_ul__a:
    print(etree.tostring(result).decode('utf-8').replace('&#13',''))


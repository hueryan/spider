from lxml import etree

html = etree.parse('xpath_test.html', etree.HTMLParser())

# 通过属性（@）定位子节点..获取父节点元素@获取其属性
result_at = html.xpath('//a[@href="link4.html"]/../@class')
print(result_at)

# 定位a节点，通过 parent::* 获取其父节点并获取其属性
result_parent = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result_parent)

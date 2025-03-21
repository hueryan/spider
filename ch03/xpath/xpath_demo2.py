from lxml import etree

# parse 获取html文件，构造 xpath 对象
html = etree.parse('./xpath_test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
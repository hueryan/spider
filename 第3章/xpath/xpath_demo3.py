from lxml import etree

html = etree.parse('./xpath_test.html', etree.HTMLParser())
# 获取所以标签
results_all = html.xpath('//*')
for result_all in results_all:
    result_all = etree.tostring(result_all)
    print('*'*20)
    print(result_all.decode('utf-8').replace('&#13', ''))

# 获取所有 li 标签
results_li = html.xpath('//li')
for result_li in results_li:
    result_li = etree.tostring(result_li)
    print('*'*20)
    print(result_li.decode('utf-8').replace('&#13', ''))
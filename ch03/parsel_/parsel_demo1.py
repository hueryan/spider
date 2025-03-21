from parsel import Selector

html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

selector= Selector(text=html)
# css、xpath方法
items = selector.css('.item-0')
print(len(items), type(items), items)
for item in items:
    text = item.xpath('.//text()').get()
    print(text)
items2 = selector.xpath('//li[contains(@class, "item-0")]')
print(len(items2), type(items2), items2)

# get 之返回第一个结果
result = selector.xpath('//li[contains(@class, "item-0")]//text()').get()
print(result)
# getall 返回所有结果
result = selector.xpath('//li[contains(@class, "item-0")]//text()').getall()
print(result)
# css 提取所有text
result = selector.css('.item-0 *::text').getall()
print(result)

result = selector.css('.item-0 ::text').getall()
print(result)
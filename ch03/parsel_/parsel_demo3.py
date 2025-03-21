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

selector = Selector(html)
# 通过re去匹配含有link节点
result = selector.css('.item-0').re('link.*')
print(result)
# 对节点的text进行匹配
result = selector.css('.item-0 *::text').re('.*item')
print(result)
result = selector.css('.item-0').re_first('<span class="bold">(.*?)</span>')
print(result)
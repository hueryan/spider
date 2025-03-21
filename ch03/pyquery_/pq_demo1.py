from pyquery import PyQuery as pq
import requests

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
# 传入文本并打印
doc = pq(html)
print(doc)

# 爬网站，返回标签
doc = pq(url='https://cuiqingcai.com')
print(doc('title'))
doc = pq(requests.get('https://cuiqingcai.com').text)
print(doc('title'))
# 传入文件
doc = pq(filename='pq_test.html')
print(doc('li'))
from pyquery import PyQuery as pq

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = pq(html)
# 通过CSS选择标签
# 选择id=container 中 class=list 的 标签为li 的节点
print(doc('#container .list li'))
print(type(doc('#container .list li')))
# 遍历通过text获取文本
for item in doc('#container .list li').items():
    print(item.text())

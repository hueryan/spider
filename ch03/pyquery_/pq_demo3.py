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
items = doc('.list')
print(items)
print(type(items))
# 查找所有li子孙节点
lis = items.find('li')
print(lis)
print(type(lis))
print('*'*100)
# 等价 Find
print(items('li'))
print(type(items('li')))

# 查找所有li儿子节点
lis = items.children()
print(lis)
print(type(lis))

# 筛选.active节点
lis = items.children('.active')
print(lis)

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
items = doc('.list')
container = items.parent()
# 直接父节点
print(type(container))
print(container)
# 祖先节点
parents = items.parents()
print(parents)
print(type(parents))
# 传入css选择器
parent = items.parents('.wrap')
print(parent)
print(type(parent))

# 兄弟节点
li = doc('.list .item-0.active')
print(li.siblings('.active'))

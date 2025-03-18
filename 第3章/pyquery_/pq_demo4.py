from pyquery import PyQuery as pq

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
# 单个节点
li = doc('.item-0.active')
print(li)
print(str(li))

# 多个节点
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(str(li).strip(), type(li))


# 获取属性
# 获取class为.item-0.active 下 a标签
# 但返回
a = doc('.item-0.active a')
print(a, type(a))
# 通过attr获取属性值
print(a.attr('href'))
print(a.attr.href)
# 返回多值
as_ = doc('a')
print(as_, type(a))
print(as_.attr('href'))
for a in as_.items():
    print(a.attr('href'))

a = doc('.item-0.active a')
print(a, a.text())

# 获取html
li = doc('.item-0.active')
print(li)
print(li.html())


html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
li = doc('li')
# 多个时html只返回第一个
print(li.html())
print(li.text())
print(type(li.text()))


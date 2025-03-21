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
# 添加、移除标签class属性值
li = doc('.item-0.active')
print(li)
li.remove_class('active')
print(li)
li.add_class('active')
print(li)

html = '''
<ul class="list">
     <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
doc = pq(html)
li = doc('.item-0.active')
print(li)
# 添加属性 name 值为 link
li.attr('name', 'link')
print(li)
# 将当前节点内东西改为text内容
li.text('changed item')
print(li)
# 将当前节点内改为html内容
li.html('<span>changed item</span>')
print(li)


html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''
doc = pq(html)
wrap = doc('.wrap')
print(wrap)
print('提取Hello, World删除<p>以及后面')
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())

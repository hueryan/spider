import re

html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

# findall
# results = re.findall(r'href="(.*?)".*?singer="(.*?)".*?>(.*?)</a>', html, re.S)
# print(results)
# for result in results:
#     print(result)
#     print(result[0], result[1], result[2])



# sub 去除 a 标签
html = re.sub('<a.*?>|</a>', '', html)
# print(html)
results = re.findall('<li.*?>(.*?)</li>', html, re.S)
# for result in results:
#     print(result.strip())

# compile
content1 = '2025-3-6 15:42'
content2 = '2025-3-7 13:54'
content3 = '2025-3-8 02:9'
pattern = "\d+:\d+"
result1 = re.sub(pattern, "", content1)
result2 = re.sub(pattern, "", content2)
result3 = re.sub(pattern, "", content3)
print(result1, result2, result3)



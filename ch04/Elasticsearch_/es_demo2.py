from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

data = {
    'title':'IT之家投票：你升级 HarmonyOS NEXT 系统了吗？',
    'url':'https://news.qq.com/rain/a/20250318A05VRA00',
}

# index 同样可以插入不用指定id，自动生成
result = es.index(index='news', body=data)
print(result)

# create 需要指定 id
# create 内部调用了 index，是对 index 方法的封装
result = es.create(index='news', id=1, body=data)
print(result)


from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

data = {
    'title':'IT之家投票：你升级 HarmonyOS NEXT 系统了吗？',
    'url':'https://news.qq.com/rain/a/20250318A05VRA00',
    'data':'2025-3-21'
}

update_data = {
    'doc' : data,
}

result = es.update(index='news', body=update_data, id=1)
print(result)

# index 同样可以更新
result = es.index(index='news', id=1, body=update_data)

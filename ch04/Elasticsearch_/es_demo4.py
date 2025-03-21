from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')
result = es.delete(index='news', id=1)
print(result)


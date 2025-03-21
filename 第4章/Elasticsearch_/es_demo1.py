from elasticsearch import Elasticsearch

# 初始化 Elasticsearch 客户端
# es = Elasticsearch(hosts='http://localhost:9200')
es = Elasticsearch(
    ['http://localhost:9200'],
    verify_certs=True
)

# # 如果已创建 忽略 400
# result = es.options(ignore_status=[400]).indices.create(index='news')
# print(result)
# 已经存在，再次创建返回 400
result = es.options(ignore_status=[400]).indices.create(index='news')
print(result)

# # 删除索引，使用 options 方法传递参数
# result = es.options(ignore_status=[400, 404]).indices.delete(index='news')
# print(result)
# 已经删除，再次删除返回 404
result = es.options(ignore_status=[400, 404]).indices.delete(index='news')
print(result)
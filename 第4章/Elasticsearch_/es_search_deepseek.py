from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

# 删除索引（如果存在）
es.options(ignore_status=[400, 404]).indices.delete(index='news')

# 创建索引并显式定义 mapping
mapping = {
    "mappings": {
        "properties": {
            "title": {
                "type": "text",
                "analyzer": "ik_max_word",      # 写入时使用细粒度分词
                "search_analyzer": "ik_max_word"  # 搜索时也使用细粒度分词
            },
            "url": {
                "type": "keyword",  # 显式定义为 keyword 类型（避免自动推断为 text）
                'fields': {
                    'keyword': {  # ⚠️ Elasticsearch 自动为 text 类型字段生成 keyword 子字段
                        'type': 'keyword',
                        'ignore_above': 256  # 仅存储前 256 字符的 keyword（可能导致长 URL 被截断）
                    }
                }

            }
        }
    }
}

# 创建索引时直接指定 mapping（一步到位）
es.indices.create(index='news', body=mapping)

# 插入数据
datas = [
    {'title': '高考结局大不同', 'url': 'https://k.sina.com.cn/article_7571064628_1c3454734001011lz9.html'},
    {'title': '进入职业大洗牌时代，“吃香”职业还吃香吗？', 'url': 'https://new.qq.com/omn/20210828/20210828A025LK00.html'},
    {'title': '乘风破浪不负韶华，奋斗青春圆梦高考', 'url': 'http://view.inews.qq.com/a/EDU2021041600732200'},
    {'title': '他，活出了我们理想的样子', 'url': 'https://new.qq.com/omn/20210821/20210821A020ID00.html'}
]

for data in datas:
    es.index(index='news', body=data)

# 强制刷新索引（确保数据立即可查）
es.indices.refresh(index='news')

# 查询所有文档（验证数据是否存在）
result = es.search(index='news', body={"query": {"match_all": {}}})
print("Total documents:", result['hits']['total']['value'])

# 搜索包含 "高考" 的文档
result = es.search(
    index='news',
    body={
        "query": {
            "match": {
                "title": "高考"
            }
        }
    }
)

print("Search results for '高考':")
for hit in result['hits']['hits']:
    print(f"Score: {hit['_score']}, Title: {hit['_source']['title']}")
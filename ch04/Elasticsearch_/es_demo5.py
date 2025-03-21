from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

# 设置中文分词器 ik_max_word
mapping = {
    'properties': {
        'title': {
            'type': 'text',
            'analyzer': 'ik_max_word',
            'search_analyzer': 'ik_max_word'
        }
    }
}
es.options(ignore_status=[400, 404]).indices.delete(index='news')
es.options(ignore_status=400).indices.create(index='news')
# 检查索引是否存在
# print(es.options().indices.exists(index='news'))


# 更新 mapping 信息、其中制定了分词的字段，包括字段的类型 type、分词器 analyzer 和搜索分词器 search_analyzer
# 指定搜索分词器 search_analyzer 为 ik_max_word 表示使用安装的中文分词插件，不指定默认为英文分词器
es.options().indices.put_mapping(index='news', body=mapping)

# 查看索引的 Mapping
print(es.options().indices.get_mapping(index='news'))

# 插入数据
datas = [
    {
        'title': '高考结局大不同',
        'url': 'https://k.sina.com.cn/article_7571064628_1c3454734001011lz9.html',
    },
    {
        'title': '进入职业大洗牌时代，“吃香”职业还吃香吗？',
        'url': 'https://new.qq.com/omn/20210828/20210828A025LK00.html',
    },
    {
        'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
        'url': 'http://view.inews.qq.com/a/EDU2021041600732200',
    },
    {
        'title': '他，活出了我们理想的样子',
        'url': 'https://new.qq.com/omn/20210821/20210821A020ID00.html',
    }
]

for data in datas:
    es.index(index='news', body=data)

es.indices.refresh(index='news')

# 获取 news 的文档数量
print(es.count(index='news'))

# # 根据关键词查询相关内容
result = es.search(index='news')
print(result)




from elasticsearch import Elasticsearch
import json

# DSL 语句查询，mathc 指定全文检索，检索的字段是 title，内容是“高考 圆梦”
# 定义 DSL 查询
dsl = {
    'query':{
        'match':{
            'title':'高考 圆梦'
        }
    }
}

es = Elasticsearch('http://localhost:9200')
# 执行查询并获取响应
result = es.search(index='news', body=dsl)

# 提取可序列化的结果（直接使用响应体的字典数据）
serializable_result = result.body  # 关键修复点：使用 .body 获取原始字典数据

# 打印格式化后的结果
print(json.dumps(serializable_result, indent=2, ensure_ascii=False))
# print(result)



result = es.search(index='news')
serializable_result = result.body
# print(json.dumps(serializable_result, indent=2, ensure_ascii=False))

# 未指定参数是默认一下
dsl = {
    'query': {
        'match_all': {}  # 匹配所有文档
    }
}
result = es.search(index='news', body=dsl)
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['spiders']
collection = db.students

print('update', '*'*50)
condition = {'name':'Dog'}
stu = collection.find_one(condition)
stu['age'] = 30
result = collection.update_one(condition, {'$set': stu})
print(result)
# 匹配数据条数和影响条数
print(result.matched_count, result.modified_count)

print('自加', '='*50)
condition = {'age':{'$gt':20}}
# 所有大于 20 的 age 增加1
result = collection.update_many(condition, {'$inc':{'age':1}})
print(result)
print(result.matched_count, result.modified_count)

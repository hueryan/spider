import pymongo

# 连接MongoDB 两种方式
client = pymongo.MongoClient(host='localhost', port=27017)
client = pymongo.MongoClient('mongodb://localhost:27017/')

# 指定 test 数据库 两种方式
db = client['spiders']
db = client.spiders

# 指定 students 集合
collection = db.students
collection = db['students']

print('插入数据', '='*50)
student = {
    'id':'2114110803',
    'name':'Jordan',
    'age':23,
    'gender':'male',
}

# 插入一个学生信息
result = collection.insert_one(student)
print(result)
# insert_id 获取id
print(result.inserted_id)


stu1 = {
    'id':'2114110812',
    'name':'Dog',
    'age':22,
    'gender':'female',
}
stu2 = {
    'id':'211411099',
    'name':'P',
    'age':23,
    'gender':'male',
}
# 插入多个学生信息
result = collection.insert_many([stu1, stu2])
print(result)
# insert_ids 获取多个id
print(result.inserted_ids)

print('查询', '='*50)
# 通过字典形式查询一个
print('find_one')
result = collection.find_one({'name':'Dog'})
print(type(result))
print(result)


print('通过 bson.objuectid 查询')
from bson.objectid import ObjectId

result = collection.find_one({'_id':ObjectId('67dbc3484cf27c5696f8ebe1')})
print(result)

# 通过字典形式查询多个
print('find')
result = collection.find({'age':22})
print(result)
for ret in result:
    print(ret)

# 条件查询
print('条件查询-比较', '='*30)
# age 大于20
results = collection.find({'age':{'$gt':20}})
print(results)
for res in results:
    print(res)

print('条件查询-正则')
results = collection.find({'name':{'$regex':'^D.*'}})
for res in results:
    print(res)

results = collection.find({'$where':'obj.fans_count == obj.follow_count'})
for res in results:
    print(res)



print('计数{} 可以添加条件查询', '='*50)
count = collection.count_documents({})
# count = collection.count_documents({'name': {'$regex':'^D.*'}})
print(count)

print('排序', '='*50)
# 关键字 升序排序 pymongo.ASCENDING, 降序 pymongo.DESCENDING
results = collection.find().sort('name', pymongo.ASCENDING)
print([res['name'] for res in results])


print('偏移', '='*50)
results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print([res['name'] for res in results])

print('limit', '='*50)
results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(3)
print([res['name'] for res in results])

print('通过ObjuctID偏移', "="* 50)
# 大于等于 ObID
results = collection.find({'_id':{'$gte':ObjectId('67dbcf5af733b910fd0892d0')}})
print([res for res in results])

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

# 删除 collection 数据
# collection.delete_many({})
# 删除 数据集
# db.drop_collection('students')
# drop collection
collection.drop()


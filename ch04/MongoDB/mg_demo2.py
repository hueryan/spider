import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['spiders']
collection = db.students

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




import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['spiders']
collection = db.students

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



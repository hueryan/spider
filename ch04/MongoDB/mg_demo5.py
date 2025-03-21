import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['spiders']
collection = db.students

# 删除 collection 数据
collection.delete_many({})
# 删除 数据集
db.drop_collection('students')
# drop collection
collection.drop()
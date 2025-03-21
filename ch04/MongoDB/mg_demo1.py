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



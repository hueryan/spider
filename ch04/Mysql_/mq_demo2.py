import pymysql

print('Insert', '='*50)
print('单个添加', '='*30)
# 单个添加
id = '2114110803'
user = 'Bob'
age = 22
db = pymysql.connect(host='localhost', user='root', password='1005', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students (id, name, age) VALUES (%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    print('Successfully Insert')
    db.commit()
except Exception as e:
    print("Failed Insert", e)
    # 回滚数据
    db.rollback()
finally:
    db.close()


print('构建字典添加', '='*30)
# 构建字典添加
data = {
    'id':'2114110723',
    'name':'Dog',
    'age':21,
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
db = pymysql.connect(host='localhost', user='root', password='1005', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful Insert')
        db.commit()
except Exception as e:
    print('Failed Insert', e)
    db.rollback()
finally:
    db.close()


print('Update', '='*50)
db = pymysql.connect(host='localhost', user='root', password='1005', port=3306, db='spiders')
cursor = db.cursor()
sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
    cursor.execute(sql, (25, 'Dog'))
    print('Successful Update')
    db.commit()
except Exception as e:
    print('Faile Update', e)
    db.rollback()
finally:
    db.close()

print('数据存在，更新数据。\n若不存在，则插入数据', '='*30)
data = {
    'id':'2114110812',
    'name':'Ener',
    'age':21,
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)
update = ','.join(["{key} = %s".format(key=key) for key in data])
sql += update
db = pymysql.connect(host='localhost', user='root', password='1005', port=3306, db='spiders')
cursor = db.cursor()
try:
    if cursor.execute(sql, tuple(data.values()) * 2):
        print('Successful Update')
        db.commit()
    else:
        print('Updated已完成')
except Exception as e:
    print('Failed Update', e)
    db.rollback()
finally:
    db.close()


import pymysql

print('Delete', '='*50)
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1005', db='spiders')
cursor = db.cursor()
table = 'students'
condition = 'age > 26'
sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    print('Successful DELETE')
    db.commit()
except Exception as e:
    print('Faile DELETE')
    db.rollback()
finally:
    db.close()


print('Select', '='*50)
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1005', db='spiders')
cursor = db.cursor()
table = 'students'
sql = 'SELECT * FROM {table} WHERE age >= 20'.format(table=table)
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    # fetchall 上面指针偏移所以 fetchall 数量是 count - 1
    # fetchall 占用内存大
    results = cursor.fetchall()
    print("Result:", results)
    print("Result Type:", type(results))
    for row in results:
        print(row)
except Exception as e:
    print('Failed Select:', e)
    db.rollback()
finally:
    db.close()


print('while', '-'*50)
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1005', db='spiders')
cursor = db.cursor()
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except Exception as e:
    print('Failed Select:', e)
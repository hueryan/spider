import pymysql

db = pymysql.connect(host='localhost', user='root', password='1005', port=3306)
# 获取MySQL操作游标
cursor = db.cursor()
# 调用 execute 执行
cursor.execute('SELECT VERSION()')
# fetchone 获取获取第一条数据
data = cursor.fetchone()
print('Database version:', data)
# 创建 spiders 数据库
cursor.execute('CREATE DATABASE IF NOT EXISTS spiders DEFAULT CHARACTER SET utf8mb4')
db.close()

# # 指定spiders数据库
db = pymysql.connect(host='localhost', user='root', password='1005', port=3306, db='spiders')
cursor = db.cursor()
# sql 语句创建 students 表
sql = 'CREATE TABLE IF NOT EXISTS students(id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY(id))'
cursor.execute(sql)
db.close()
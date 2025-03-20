# 数据的存储

## text_load

### TXT 文本文件存储

- txt_demo1：通过 `with open(FILENAME, "model", encoding='utf-8') as f` 将内容写入文本

  | model | model |
  | ----- | ----- |
  | r     | w     |
  | rb    | wb    |
  | r+    | w+    |
  | rb+   | wb+   |
  | a     | ab    |
  | a+    | ab+   |

### JSON 文件存储

json数据使用双引号引用

- json_demo1：`loads` 字符串=> 对象。`dumps` JSON对象=>字符串

  通过索引获取对应内容

- json_demo2：加载json文件，read在loads加载。也可以直接load文件

- json_demo3：将data写入文件。`json.dumps(str[, index])` index代表缩进字符的个数，当有中文时添加参数 `ensure_ascii=False` 

### CSV 文件存储

- csv_demo1：open时候添加参数 `newline=''` 即可删除空行

  `csv.writer(csvfile, delimiter=' ')` 修改数据间的间隔符

  writerows传入二维数据

- csv_demo2：字典形式传入。pandas.DataFrame.to_csv()写入文件

- csv_demo3：csv、pd读取、以及pd对象转换成list

  

  

## MySQL 存储

安装 `pip install pymysql` [_](https://setup.scrape.center/pymysql) 

- mq_demo1：连接MySQL数据库、创建表
- mq_demo2：增、改
- mq_demo3：删、查

## MongoDB

`pip install pymongo` [_](http://setup.scrape.center/mongodb) [_](http://setup.scrape.center/mongodb) 

- mg_demo1：连接MongoDB、指定数据库、指定集合、插入数据、查询数据、计数

  条件查询

  比较符号

  | 符号 | 含义       | 实例                      |
  | ---- | ---------- | ------------------------- |
  | $lt  | 小于       | {'age':{'$lt':20}}        |
  | $gt  | 大于       | {'age':{'$gt':20}}        |
  | $lte | 小于等于   | {'age':{'$lte':20}}       |
  | $gte | 大于等于   | {'age':{'$gte':20}}       |
  | $ne  | 不等于     | {'age':{'$ne':20}}        |
  | $in  | 在范围内   | {'age':{'$in':[20, 23]}}  |
  | $nin | 不在范围内 | {'age':{'$nin':[20, 23]}} |

  功能符号

  | 符号    | 含义           | 实例                                            | 实例含义             |
  | ------- | -------------- | ----------------------------------------------- | -------------------- |
  | $regex  | 匹配正则表达式 | {'name':{'$regex':'^D.*'}}                      | name 以 D 为开头     |
  | $exists | 属性是否存在   | {'name':{'$exists':True}}                       | 存在name属性         |
  | $type   | 类型判断       | {'age':{'$type':'int'}}                         | age类型为int         |
  | $mod    | 数字模操作     | {'age':{'$mod':[5, 0]}}                         | age 模 5 余 0        |
  | $text   | 文本查询       | {'$text':{'$search':'Dog'}}                     | Dog 字符串           |
  | $where  | 高级条件查询   | {'$where':'obj.fans_count == obj.follow_count'} | 自身粉丝数等于关注数 |

  | 方法                                                         | 描述                                   |
  | ------------------------------------------------------------ | -------------------------------------- |
  | collection.count_documents({})                               | 获取collection的个数 {} 可加入查询条件 |
  | pymongo.ASCENDING                                            | 升序排序                               |
  | pymongo.DESCENDING                                           | 降序                                   |
  | collection.find().sort('name', pymongo.ASCENDING).skip(2)    | 偏移2位                                |
  | collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(3) | 限制3个结果                            |

  不要使用大偏移量查询，通过上次 `_id` 查询

  update_one(condition, {'$set':stu})

  age + 1

  update_many(condition, {'$inc':{'age':1}})

  | 方法                 | ...            |
  | -------------------- | -------------- |
  | find_one_and_delete  | create_index   |
  | find_one_and_replace | create_indexes |
  | find_one_and_update  | drop_index     |

  

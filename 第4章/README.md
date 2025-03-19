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

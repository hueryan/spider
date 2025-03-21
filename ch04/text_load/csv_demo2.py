import csv
import pandas as pd
# 传入字典
with open('data_dict.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'10001', 'name':'Mike', 'age':20})
    writer.writerow({'id':'10002', 'name':'Bob', 'age':22})
    writer.writerow({'id':'10003', 'name':'Jordan', 'age':21})

# 追加
with open('data_dict.csv', 'a', newline='') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id':'10004', 'name':'Durant', 'age':22})

# 中文写入
with open('data_dict.csv', 'a', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id':'10004', 'name':'王伟', 'age':22})


data = [
    {'id':'10001', 'name': 'Mike', 'age': 20},
    {'id':'10002', 'name': 'Bob', 'age': 22},
    {'id':'10003', 'name': 'Jordan', 'age': 21},
]
# 将data转化成 DataFrame 对象
df = pd.DataFrame(data)
df.to_csv('data_dict_pandas.csv', index=False)
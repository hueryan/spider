import csv
import pandas as pd

print('csv.reader', '='*50)
with open('data_dict.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

print('读取df对象', '='*50)
df = pd.read_csv('data_dict.csv')
print(df)

# 只读取文件数据，通过把df转化成列表或元组
print('转化列表', '='*50)
data = df.values.tolist()
print(data)

print('直接遍历', '='*50)
for index, row in df.iterrows():
    print(row.tolist())

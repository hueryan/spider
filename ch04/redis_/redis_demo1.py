from redis import StrictRedis

# 连接 redis
# 默认 host=localhost port=6379 db=0 password=None
redis = StrictRedis(host='localhost', port=6379, db=0)

# 选择 8 号数据库
redis.select(8)

# set 设置键值对
redis.set('name', 'Bob')
# get键 获取值
print(redis.get('name'))

print(redis.ttl('name'))

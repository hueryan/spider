from redis import StrictRedis, ConnectionPool

# 通过 ConnectionPool 连接
pool = ConnectionPool(host='localhost', port=6379, db=0)
redis = StrictRedis(connection_pool=pool)

# 选择 8 号数据库
url = 'redis://@localhost:6379/8'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
redis.flushdb()
print(redis.dbsize())

redis.decr('age', 5)
print(redis.get('age'))
redis.flushdb()

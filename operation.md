```shell
conda create -n spider python=3.10
conda activate spider
```

```bash
pip install requests  # 安装 requests
pip install httpx[http2]
pip install aiohttp
pip install cchardet aiodns # 字符编码检测库 cchardet, 加速 DNS 解析库 aiodns
pip install pyquery 
```







```shell
git init 
git add .
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:hueryan/spider.git
git push -u origin main
```



### MongoDB 

[zip安装](https://www.mongodb.com/try/download/community-kubernetes-operator) 

[shell安装](https://www.mongodb.com/try/download/shell) 

```
mongod  --install --dbpath D:\ProgramFiles\mongodb\data --logpath D:\ProgramFiles\mongodb\logs\mongodb.log

mongosh --host=localhost --port=27017
```



### Redis

[GitHub](https://github.com/MicrosoftArchive/redis/releases) 

```shell
redis-server --service-install redis.windows.conf # 安装 Redis 服务

redis-cli [-h 127.0.0.1 -p 6379] # Redis 客户端
```

Redis默认拥有16个数据库，初始默认使用0号库，在命令行中通过`select`命令将数据库切换到8号数据库：

在命令中通过`set`命令设置键值，通过`get`命令取出键值

```shell
select 8
set key1 hello
get key1
shutdown # 关闭服务

redis-server --service-OP
OP: uninstall 卸载服务
    stop	停止服务
```

三种打开服务方法

```shell
redis-server # 命令行启动 redis 服务。通过cmd显示

redis-server --service-start

Win+R -> services.msc -> Redis 
```


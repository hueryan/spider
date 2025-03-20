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



MongoDB 

[zip安装](https://www.mongodb.com/try/download/community-kubernetes-operator) 

[shell安装](https://www.mongodb.com/try/download/shell) 

```
mongod  --install --dbpath D:\ProgramFiles\mongodb\data --logpath D:\ProgramFiles\mongodb\logs\mongodb.log

mongosh --host=localhost --port=27017
```


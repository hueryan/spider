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

### **ElasticSearch**

[elasticSearch](https://www.elastic.co/cn/downloads/past-releases#elasticsearch) 

修改指定版本JDK, `D:\ProgramFiles\elasticsearch-8.17.3\bin\elasticsearch-env-.bat` 40行

```diff
- if defined ES_JAVA_HOME (
-   set JAVA="%ES_JAVA_HOME%\bin\java.exe"
-   set JAVA_TYPE=ES_JAVA_HOME
- 
-   if not exist !JAVA! (
-     echo "could not find java in !JAVA_TYPE! at !JAVA!" >&2
-     exit /b 1
-   )
- 
-   rem check the user supplied jdk version
-   !JAVA! -cp "%ES_HOME%\lib\java-version-checker\*" "org.elasticsearch.tools.java_version_checker.JavaVersionChecker" || exit /b 1
- ) else (
-   rem use the bundled JDK (default)
-   set JAVA="%ES_HOME%\jdk\bin\java.exe"
-   set "ES_JAVA_HOME=%ES_HOME%\jdk"
-   set JAVA_TYPE=bundled JDK
- )

+ set JAVA_HOME=D:\ProgramFiles\Java\jdk-17
+ if "%JAVA_HOME%" == "" (
+   set JAVA="%ES_HOME%\jdk\bin\java.exe"
+   set JAVA_HOME="%ES_HOME%\jdk"
+   set JAVA_TYPE=bundled jdk
+ ) else (
+   set JAVA="%JAVA_HOME%\bin\java.exe"
+   set JAVA_TYPE=JAVA_HOME
+ )
```

修改 elasticsearch.yml 文件

```diff
- xpack.security.enabled: true
- xpack.security.http.ssl:
-   enabled: true

+ xpack.security.enabled: false
+ xpack.security.http.ssl:
+   enabled: false
```

服务安装等

```diff
elasticsearch-service install
+                     remove
+					  start
+					  stop
```

启动服务

```shell
elasticsearch # 命令行启动 elasticsearch 服务。通过cmd显示

elasticsearch-service start

Win+R -> services.msc -> Elasticsearch 8.17.3
```

通过 `localhost:9200` 进入

在 `\bin` 文件中通过 `.\elasticsearch-reset-password -u elastic` 获取账号密码






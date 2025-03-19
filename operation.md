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



撤销 git add 和 git commit

```
git reset --sofr HEAD^
```

这样就成功撤销了commit，如果想要连着工作区代码也撤销的话，–soft改为–hard（删除工作空间的改动代码，**会导致本次改动的代码丢失**）。

HEAD^ 表示上一个版本，即上一次的commit，也可以写成HEAD~1
如果进行两次的commit，想要都撤回，可以使用HEAD~2

–soft
不删除工作空间的改动代码 ，撤销commit，不撤销git add file

–hard
删除工作空间的改动代码，撤销commit且撤销add，**会导致本次改动的代码丢失**

另外一点，如果commit注释写错了，先要改一下注释，有其他方法也能实现

```
git commit --amend
这时候会进入vim编辑器，修改完成你要的注释后保存即可。
```


网页通过一次次Ajax请求返回数据，进行渲染

[Ajax 实例](https://www.w3school.com.cn/js/js_ajax_http_send.asp) 

从发送Ajax请求到网页等新的过程分为3步——发送请求、解析内容、渲染网页。

### Ajax 分析方法

`Network` -> `Headers` -> `Request Headers` -> `{'x-requested-with':'XMLHttpRequest'}` 请求为Ajax

`Network` -> `Rreview` 查看相应内容。JS接收到这些数据，在执行相应的渲染方法。

`Response` 也可观察真实数据。



- demo: 爬取网站存储到MongoDB、本地

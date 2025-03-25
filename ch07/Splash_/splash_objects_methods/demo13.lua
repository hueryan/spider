-- 此方法可以执行 JavaScript 代码并返回最后一条 JavaScript 语句的返回结果，使用方法如下：
result = splash:evaljs(js)
-- 获取页面标题
local title = splash:evaljs("document.title")
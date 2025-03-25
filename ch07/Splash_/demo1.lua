function main(splash, args)
  splash:go("http://www.baidu.com")
  splash:wait(0.5)
--   通过 evaljs 传入JS脚本  document.title返回网页标题
  local title = splash:evaljs("document.title")
--   返回值可以是字典，也可以是 str。最后转化为 Splash 的 HTTP 响应
  return {title=title}
end

function main(splash, args)
  splash:go("http://www.baidu.com")
--   禁用JS
  splash.js_enabled = false
--   重新调用js，抛出异常
  local title = splash:evaljs("document.title")
  return {title="title"}
end
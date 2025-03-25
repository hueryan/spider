-- autoload 方法声明了一个 JavaScript 方法，然后通过 evaljs 方法来执行此 JavaScript 方法
function main(splash, args)
  splash:autoload([[function get_document_title(){return document.title;}
  ]])
  splash:go("https://www.baidu.com")
  return splash:evaljs("get_document_title()")
end


-- 使用 autoload 方法加载某些方法库，如 jQuery
function main(splash, args)
  assert(splash:autoload("https://code.jquery.com/jquery-2.1.3.min.js"))
  assert(splash:go("https://www.taobao.com"))
  local version = splash:evaljs("$.fn.jquery")
  return 'JQuery version: ' .. version
end
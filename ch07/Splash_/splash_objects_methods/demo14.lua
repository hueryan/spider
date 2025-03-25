-- runjs 方法先声明了一个 JavaScript 定义的方法，然后通过 evaljs 方法来调用得到的结果
function main(splash, args)
  splash:go("https://www.baidu.com")
  splash:runjs("foo = function() {return 'bar'}")
  local result = splash:evaljs("foo()")
  return result
end
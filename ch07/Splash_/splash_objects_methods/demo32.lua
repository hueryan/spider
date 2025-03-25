-- 首先访问了百度，然后选中了搜索框，随后调用了 send_text() 方法填写了文本，然后返回网页截图。
function main(splash)
  splash:go("https://www.baidu.com/")
  input = splash:select("#kw")
  input:send_text('Splash')
  splash:wait(3)
  return splash:png()
end
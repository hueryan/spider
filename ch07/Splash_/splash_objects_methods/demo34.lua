-- 首先选中了页面的输入框，输入了文本，然后选中了提交按钮，调用了 mouse_click() 方法提交查询，然后页面等待三秒，返回截图，
function main(splash)
  splash:go("https://www.baidu.com/")
  input = splash:select("#kw")
  input:send_text('Splash')
  submit = splash:select('#su')
  submit:mouse_click()
  splash:wait(3)
  return splash:png()
end
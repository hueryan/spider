-- 设置了一个定时任务，0.2 秒的时候获取网页截图，然后等待 1 秒，1.2 秒时再次获取网页截图，访问的页面是淘宝，最后将截图结果返回。
function main(splash, args)
  local snapshots = {}
  local timer = splash:call_later(function()
    snapshots["a"] = splash:png()
    splash:wait(1.0)
    snapshots["b"] = splash:png()
  end, 0.2)
  splash:go("https://www.taobao.com")
  splash:wait(3.0)
  return snapshots
end
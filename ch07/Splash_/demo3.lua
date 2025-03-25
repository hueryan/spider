function main(splash, args)
  local example_urls = {"www.baidu.com", "www.taobao.com", "www.zhihu.com"}
  local urls = args.urls or example_urls
  local results = {}
  for index, url in ipairs(urls) do
--       .. 字符串拼接
--       go 方法返回加载页面的结果状态，若返回 4xx 或 5xx，ok被置空
    local ok, reason = splash:go("http://" .. url)
    if ok then
--         sleep(2),当 Splash 执行到此，转向处理其他任务。在等待参数指定的时间后再回来继续处理
      splash:wait(2)
      results[url] = splash:png()
      end
    end
  return results
end
function main(splash)
--  设置超时时间
  splash.resource_timeout = 0.1
  assert(splash:go("http:www.baidu.com"))
  return splash:png()
end
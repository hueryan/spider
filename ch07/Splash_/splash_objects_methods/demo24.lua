function main(splash, args)
  splash:go("https://www.baidu.com")
  return splash:get_cookies()
end
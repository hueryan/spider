function main(splash)
  splash:set_user_agent('Splash')
  splash:go("http://httpbin.org/get")
  return splash:html()
end
function main(splash, args)
  splash:go("https://httpbin.org/get")
  return splash:html()
end
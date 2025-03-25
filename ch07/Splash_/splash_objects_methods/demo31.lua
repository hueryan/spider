function main(splash)
  splash:set_custom_headers({["User-Agent"] = "Splash",
     ["Site"] = "Splash",
  })
  splash:go("http://httpbin.org/get")
  return splash:html()
end
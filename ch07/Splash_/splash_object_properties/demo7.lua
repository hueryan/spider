function main(splash, args)
  splash.images_enabled = false
  assert(splash:go('https://www.jd.com'))
  return {png=splash:png()}
end
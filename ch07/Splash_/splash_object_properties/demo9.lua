function main(splash, args)
  assert(splash:go('https://www.taobao.com'))
--   向下滚动400
  splash.scroll_position = {y=400}
--   左右滚动
  splash.scroll_position = {x=100,y=200}
  return {png=splash:png()}
end
-- Splash 支持将main方法的第二个参数直接设置args
function main(splash, args)
  local url = args.url
end


-- 等价以上内容
function main(splash)
  local url = splash.args.url
end
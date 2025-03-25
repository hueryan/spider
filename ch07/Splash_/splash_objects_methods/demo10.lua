function main(splash, args)
  local ok, reason = splash:go{"http://www.httpbin.org/post", http_method="POST", body="name=Germmey"}
  if ok then
    return splash:html()
   end
end
-- 通过 CSS 选择器选中了节点的正文内容，随后遍历了所有节点，将其中的文本获取下来。
function main(splash)
  local treat = require('treat')
  assert(splash:go("http://quotes.toscrape.com/"))
  assert(splash:wait(0.5))
  local texts = splash:select_all('.quote .text')
  local results = {}
  for index, text in ipairs(texts) do
    results[index] = text.node.innerHTML
  end
  return treat.as_array(results)
end
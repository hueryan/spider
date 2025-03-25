-- 声明了一个 JavaScript 定义的方法，然后在页面加载成功后调用了此方法计算出了页面中 div 节点的个数。
function main(splash, args)
  local get_div_count = splash:jsfunc([[function () {
    var body = document.body;
    var divs = body.getElementsByTagName('div');
    return divs.length;
  }
  ]])
  splash:go("https://www.baidu.com")
  return ("There are % s DIVs"):format(get_div_count())
end
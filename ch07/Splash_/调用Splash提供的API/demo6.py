import requests
from urllib.parse import quote

lua = '''
function main(splash)
    return 'hello'
end
'''

url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)



# 这里我们用 Python 中的三引号将 Lua 脚本包括起来，
# 然后用 urllib.parse 模块里的 quote() 方法将脚本进行 URL 转码，
# 随后构造了 Splash 请求 URL，将其作为 lua_source 参数传递，这样运行结果就会显示 Lua 脚本执行后的结果。
import requests
from urllib.parse import quote

lua = '''
function main(splash, args)
  local treat = require("treat")
  local response = splash:http_get("http://httpbin.org/get")
	return {html=treat.as_string(response.body),
    url=response.url,
    status=response.status
    }
end
'''
url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)
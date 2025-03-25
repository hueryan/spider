import requests

url = 'http://localhost:8050/render.html?url=https://www.baidu.com'
response = requests.get(url)
print(response.text)


import requests
url = 'http://localhost:8050/render.html?url=https://www.taobao.com&amp;wait=5'
response = requests.get(url)
print(response.text)
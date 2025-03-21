import requests
import re

r_text = requests.get('https://ssr1.scrape.center/')
pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
# 获取电影名称
titles = re.findall(pattern, r_text.text)
# print('titles: ', titles)

# 用 get 爬取网站图标
r_ico = requests.get('http://scrape.center/favicon.ico')
with open('t2_r_ico_favicon.ico', 'wb') as f:
    f.write(r_ico.content)
# print(r_ico.text)
# print(r_ico.content)

headers = {
    "User-Agent":'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36'
}
r_get = requests.get('http://ssr1.scrape.center/', headers=headers)
# print(r_ssr1.text)

data = {
    'name' : 'germey',
    'age' : 18,
}
r_post = requests.post('http://httpbin.org/post', data=data, headers=headers)
# print(r_post.text)
# print(r_post.url)

# 状态码
# exit() if not r_text.status_code == requests.codes.ok else print('Request Successfully')

# 上传文件
files = {'file':open('t2_r_ico_favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files, headers=headers)
# print(r.text)

# r_cookies = requests.get('https://baidu.com').cookies
# for key, val in r_cookies.items():
#     print(key + '=' + val)

headers_github = {
    'Cookie':'_octo=GH1.1.1774316005.1738660622; _device_id=d9d4571ab3020c37a0d71b441676f5f0; saved_user_sessions=96642602%3AMSecnrVikk3W02EW9nv_cQ0meGI1VW5H58gw4fDpIOEabxJI; user_session=MSecnrVikk3W02EW9nv_cQ0meGI1VW5H58gw4fDpIOEabxJI; __Host-user_session_same_site=MSecnrVikk3W02EW9nv_cQ0meGI1VW5H58gw4fDpIOEabxJI; logged_in=yes; dotcom_user=hueryan; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; cpu_bucket=lg; preferred_color_mode=light; tz=Asia%2FShanghai; _gh_sess=hhI%2BmSaQ7jVujODuFwd5j8hH5mZMHMijOOO979uGcWiUW4Fxe9BKwh3Nnw8e85%2BMpONn%2FuT1uwwWxvcJzeNyG6mXTs5s3Wm5%2B7uO8tUso9tkxmgUaG5hTj5IY%2FBkjGVFhYDqGAzRN1UEVMsHARXEsgMksGUfnMAQssnP0uPQzzumMkuaqV8xZnpKHwPOb4vWTx4Mp3aha2XwzZS6EuuYDd%2FDe5S5NtCa3U1helLPVossrtOarCuDgAvWJtIfFFne7G0HUy5BkRItDh25cHFBqTcZAx%2FPrUWZf5UWropxMD9NENbfZ7nQB9QhufQbYbxW1ae%2Fjtu2aQLmecLQTEC813soa6GO8cOPz8GsVv9P7KrHpaT3aZI1XSGLgmoi7pwC4XzrrWRX6N1l5RbB8r6nU%2FVvzlA%3D--m1ag%2BmbNY%2FdG3r78--IO5kaAeM8PNs3gD4%2Fuw0ug%3D%3D'

}
r_github_cookie = requests.post('http://github.com', data=data, headers=headers_github)
# print(r_github_cookie.text)

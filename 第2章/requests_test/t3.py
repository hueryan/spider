import requests
import urllib3

url_ssr2 = 'http://ssr2.scrape.center/'

# # 忽略警告
# urllib3.disable_warnings()
# response = requests.get(url_ssr2, verify=False)
# print(response.status_code)
#
# # 捕获警告到日志方式忽略警告
# import logging
# logging.captureWarnings(True)
# response = requests.get(url_ssr2, verify=False)
# print(response.status_code)

# # 超时
# url_httpbin_get = 'http://httpbin.org/get'
# response = requests.get(url_ssr2, timeout=(2,2))
# print(response.status_code)

# # 窗口认证
# url_ssr3_admin = 'http://admin:admin@ssr3.scrape.center/'
# url_ssr3 = 'http://ssr3.scrape.center/'
# response = requests.get(url_ssr3, auth=('admin','admin'))
# print(response.status_code)

from requests import Session, Request
url_post = 'https://www.httpbin.org/post'
data = {'name':'germey'}
headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36'
}
s = Session()
req = Request('POST', url_post, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
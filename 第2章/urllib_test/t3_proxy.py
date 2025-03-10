# from urllib.request import ProxyHandler, build_opener
# from urllib.error import URLError
#
# # 配置代理（确保地址和端口正确）
# proxy_handler = ProxyHandler({
#     # 'http': 'http://10.10.8.41:8080',
#     'https': 'http://127.0.0.1',  # 注意此处使用 http://
# })
#
# opener = build_opener(proxy_handler)
# opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')]
#
# try:
#     response = opener.open('http://www.baidu.com', timeout=10)
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(f"连接失败: {e.reason}")

import urllib.request
url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)
with open('t3_baidu.html', 'w', encoding='utf-8') as f:
    f.write(response.read().decode('utf-8'))
print(response.read().decode('utf-8'))

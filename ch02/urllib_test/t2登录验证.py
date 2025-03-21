from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'admin'
password = 'admin'
url = 'https://ssr3.scrape.center/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, uri=url, user=username, passwd=password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    # print(result.status)
    filename = f't2_ssr3.scrape.center.html'
    print(filename)
    html = result.read().decode('utf-8')
    # print(html)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
except URLError as e:
    print(e.reason)
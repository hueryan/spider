import requests
import urllib3

urllib3.disable_warnings()

url = 'http://ssr3.scrape.center/'
url_ssr2 = 'http://ssr2.scrape.center/'
url_s = "https://static1.scrape.center/"

response = requests.get(url, auth=('admin', 'admin'))
print(response.status_code)

u = 'https://static1.scrape.center/'
res = requests.get(u, verify=False)
print(res)
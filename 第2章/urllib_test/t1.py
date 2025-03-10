import urllib.request
import urllib.parse

response = urllib.request.urlopen('http://www.pthon.org')
# response = urllib.request.urlopen('https://ssr3.scrape.center/')

print(response.status)
print(type(response))
print(response.getheaders())
print(response.getheader('Content-Type'))
# print(response.read().decode('utf-8'))

# data = bytes(urllib.parse.urlencode({'name':'germey'}), encoding='utf-8')
# response = urllib.request.urlopen('http://www.httpbin.org/post', data)
# print(response.read().decode('utf-8'))



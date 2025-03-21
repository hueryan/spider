import requests
url = 'https://www.httpbin.org/get'
data = {
    'name':'germey',
    'age':18,
}
r = requests.get(url, params=data)
print(r.status_code)
# print(r.text)
print(r.json())
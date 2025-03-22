import requests

url = 'https://spa1.scrape.center/'
result = requests.get(url)
print(result.text)
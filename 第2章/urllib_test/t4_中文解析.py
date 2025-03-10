from urllib.parse import unquote, quote
url_qu = 'http://localhost:8080/ai/generate?message=“ioc容器是什么”'
print(quote(url_qu))


url_unqu = 'http://localhost:8080/ai/generate?message=%E2%80%9Cioc%E5%AE%B9%E5%99%A8%E6%98%AF%E4%BB%80%E4%B9%88%E2%80%9D'
print(unquote(url_unqu))

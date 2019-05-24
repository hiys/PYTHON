import requests
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
           'Rerferer':'http://www.baidu.com'}
r = requests.get('http://www.goubanjia.com',
                 headers=headers,proxies={})
print(r.text)


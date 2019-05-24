#! -*- coding:utf8 -*-
import urllib.request
proxy = urllib.request.ProxyHandler(
    {'http':'94.242.58.14:10010'})

opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)
response = opener.open('http://2018.ip138.com/ic.asp').read()
print(response)
page = response.decode('gb18030')
print(page)
#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
/usr/local/lib/python3.6/urllib/request.py 
 324 class Request:
 325 
 326     def __init__(self, url, data=None, headers={},
 327                  origin_req_host=None, unverifiable=False,
 328                  method=None):
 329         self.full_url = url
 330         self.headers = {}
 331         self.unredirected_hdrs = {}
 332         self._data = None
 333         self.data = data
CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie、
向传出的HTTP 请求添加cookie的对象。
整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失
如果需要和本地文件交互，就用
 MozillaCookjar() 或 LWPCookieJar()。
如果我们对cookie有定制的需要，那么我们也要借助
HTTPCookieProcess处理器来处理

保存cookie到文件，使用MozillaCookjar()

"""
#! -*- coding: utf8 -*-

import  http.cookiejar

import  urllib.request
import  urllib.parse
import  sys
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

#----------------使用CookieJar获取cookie值 ----------
cj = http.cookiejar.CookieJar()

print(cj,type(cj),sep = '\n',end='\n-----cj-------\n')
#<CookieJar[]>
#<class 'http.cookiejar.CookieJar'>


handle = urllib.request.HTTPCookieProcessor(cj)
print(handle, type(handle), sep='\n', end='\n-----handle -------\n')
#<urllib.request.HTTPCookieProcessor object at 0x7f4c47949978>
#<class 'urllib.request.HTTPCookieProcessor'>


opener = urllib.request.build_opener(handle)
print(opener, type(opener), sep='\n', end='\n-----opener -------\n')
#<urllib.request.OpenerDirector object at 0x7f4c3ff8b128>
#<class 'urllib.request.OpenerDirector'>


data = {'username': 'admin', 'password': 'admin'}
resp = opener.open("http://192.168.0.254:8888/login",
  data=urllib.parse.urlencode(data).encode('utf8'))

print(resp, type(resp),sep = '\n',end='\n-----resp -------\n')
#<http.client.HTTPResponse object at 0x7f77fd6b2be0>
#<class 'http.client.HTTPResponse'>

print(resp.read(), end = '\n-------- resp.read ----------\n')
#b'{"code": 0, "msg": "OK HAHAhaha ---ok"}'

response = opener.open('http://192.168.0.254:8888/')
print(response.read(), end = '\n-------- response.read ----------\n')
#b'Hello, world'

#使用MozillaCookjar(),获取网站的cookie并保存cookie到文件中

def save_cookie(url, cookie_filename):
  cookie =  http.cookiejar.MozillaCookieJar(cookie_filename)
  print(cookie,end='\n----------cookie -------\n')
  #<MozillaCookieJar[]>

  handler = urllib.request.HTTPCookieProcessor(cookie)
  opener = urllib.request.build_opener(handler)
  resp = opener.open(url)

  cookieStr = ''
  for item in cookie:
    cookieStr = cookieStr + item.name + '=' + item.value + ';'
  print(cookieStr,end='\n----------cookieStr -------\n')
  cookie.save()

url = 'http://192.168.0.254:8888/'
header = {
  'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
}

cookie_filename = 'cookie.txt'
req = urllib.request.Request(url, headers=header)
print(req, type(req),sep = '\n',end='\n-----req -------\n')

save_cookie(req, cookie_filename)

print('\n============================ -----------\n')


url = 'http://192.168.0.254:8888/login'
header = {
  'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
}
data = {'username': 'admin', 'password': 'admin'}
data=urllib.parse.urlencode(data).encode('utf8') # 转成url编码

cookie_filename = 'cookie.txt'

    # 获取cookie对象
cookie = http.cookiejar.MozillaCookieJar(cookie_filename)

    # 构建一个cookie的处理器
handler = urllib.request.HTTPCookieProcessor(cookie)

    # 获取一个opener对象
opener = urllib.request.build_opener(handler)

# 获取一个请求对象
req = urllib.request.Request(url, data)
    # 给opener添加请求头，使用的是元组的方式
opener.addheaders = [('User-Agent',
      "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0")]

    # 请求服务器，返回响应对象，这时cookie已经随着resp对象携带过来了
resp = opener.open(req)

cookie.save()

request = opener.open("http://192.168.0.254:8888/")
print(request, end='\n-----request -------\n')

response = urllib.request.urlopen("http://192.168.0.254:8888/").read()

fhandle = open('./templates/x2.html','wb')
fhandle.write(response)
fhandle.close()

with open('./templates/x2.html','rb') as fobj:
  data = fobj.readlines()
  print(data,end='\n\n')
print('\n-------2---------\n')


if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)



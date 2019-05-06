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


url = 'http://192.168.0.254:8888/login'
header = {
  'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
}

#----------------使用CookieJar获取cookie值 ----------
#cj = http.cookiejar.CookieJar()

cookie_filename = 'cookie.txt' # 保存cookie的文件名称
    # 获取cookie对象
cookie = http.cookiejar.MozillaCookieJar(cookie_filename)

    # 构建一个cookie的处理器
handler = urllib.request.HTTPCookieProcessor(cookie)

    # 获取一个opener对象
opener = urllib.request.build_opener(handler)


data = {'username': 'admin', 'password': 'admin'}
data=urllib.parse.urlencode(data).encode('utf8') # 转成url编码

#data = {'username':'admin','password':'admin'}
#postdata = urllib.parse.urlencode(data).encode('utf-8')
#request = urllib.request.Request(url,data=postdata, headers=header)

# 获取一个请求对象
req = urllib.request.Request(url, data)

    # 给opener添加请求头，使用的是元组的方式
opener.addheaders = [('User-Agent',
      "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0")]

#response = urllib.request.urlopen(request).read()

    # 请求服务器，返回响应对象，这时cookie已经随着resp对象携带过来了
resp = opener.open(req)

cookie.save()
#[root@room9pc01 spider]# cat   cookie.txt
# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.

#192.168.0.254	FALSE	/	FALSE	1559620227	uid	"2|1:0|10:1557028227|3:uid|8:YWRtaW4=|1412a65ecfcb6fb2b2f1bf705723dd0446b5ff0bafd4bb05908bbf4f8e78e13a"

response = resp.read()
print(response, end='\n--------resp.read ----------\n')
#b'{"code": 0, "msg": "OK HAHAhaha ---ok"}'

response = opener.open('http://192.168.0.254:8888/').read()
print(response, end = '\n-------- response ----------\n')
#b'Hello, world'

with open('./templates/login_cookie.html','wb') as fobj:
  fobj.write(response)
print('\n------- login_cookie.html  ---------\n')
#[root@room9pc01 spider]# cat  templates/login_cookie.html 
#Hello, world



if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)



#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
/usr/local/lib/python3.6/urllib/request.py 
 324 class Request:
 325 
 326     def __init__(self, url, data=None, headers={},
 327                  origin_req_host=None, unverifiable=False,
 328                  method=None):
[root@room9pc01 spider]# ls  /usr/local/lib/python3.6/site-packages/requests/
adapters.py  compat.py      hooks.py            packages.py      structures.py
api.py       cookies.py     __init__.py         __pycache__      utils.py
auth.py      exceptions.py  _internal_utils.py  sessions.py      __version__.py
certs.py     help.py        models.py           status_codes.py

[root@room9pc01 spider]# ls  /usr/local/lib/python3.6/site-packages/requests-2.21.0.dist-info/
INSTALLER  LICENSE  METADATA  RECORD  top_level.txt  WHEEL

[root@V0 ~]# cat   /usr/local/lib/python3.6/site-packages/README.txt 
This directory exists so that 3rd party packages can be installed
here.  Read the source for site.py for more details.
此目录存在，因此可以在此处安装第三方软件包。
有关详细信息，请阅读site.py的源文件。
parameter       英 [pəˈræmɪtə(r)]
       n.决定因素;规范;范围
"""
#! -*- coding:utf8 -*-
import  requests
import  sys
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

response = requests.get('http://192.168.0.254:8888/')
print(response.text)
#<!DOCTYPE html>
#<!--STATUS OK-->
#<html lang="zh-CN">
#<head>
#<meta charset="UTF-8">
#<link rel="icon" href="/favicon.ico">
#<title>Title标题</title>
#</head>
#<body>
#<div>
#<a href="/xshell6.png" target="_blank">_blank点击xshell6.png</a>
#<a href="javascript:alert('这是弹出对话框的内容');">点击链接</a>
#</div>
#<form action="/login" method="post">
#<input name="username">
#<input name="password">
#<button type="submit">提交submit</button>
#</form>
#</body>
#</html>

resp = requests.get('http://httpbin.org/get')
print(resp.text, type(resp.text),sep='\n------resp.txt ------\n',end='\n\n')
#{
#  "args": {}, 
#  "headers": {
#    "Accept": "*/*", 
#    "Accept-Encoding": "gzip, deflate", 
#    "Host": "httpbin.org", 
#    "User-Agent": "python-requests/2.21.0"
#  }, 
#  "origin": "58.62.92.104, 58.62.92.104", 
#  "url": "https://httpbin.org/get"
#}
#
#------resp.txt ------
#<class 'str'>



print(resp.json(),type(resp.json()),
  sep='\n------resp.json() ------\n', end='\n\n')
#{'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.21.0'}, 'origin': '58.62.92.104, 58.62.92.104', 'url': 'https://httpbin.org/get'}
#------resp.json() ------
#<class 'dict'>



payload = {'key1':'value1',
           'key2':['v1','v2'],
           'wd':'国家食品药品监督管理局'
           }

r = requests.get("http://httpbin.org/get",params=payload)
obj = r.json()
print(obj, end='\n\n')
#{'args': {'key1': 'value1', 'key2': ['v1', 'v2'], 'wd': '国家食品药品监督管理局'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.21.0'}, 'origin': '58.62.92.104, 58.62.92.104', 'url': 'https://httpbin.org/get?key1=value1&key2=v1&key2=v2&wd=国家食品药品监督管理局'}


if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)




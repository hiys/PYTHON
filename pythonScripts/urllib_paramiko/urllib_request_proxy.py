#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
/usr/local/lib/python3.6/urllib/request.py 
 324 class Request:
 325 
 326     def __init__(self, url, data=None, headers={},
 327                  origin_req_host=None, unverifiable=False,
 328                  method=None):
http://2019.ip138.com/ic.asp
您的IP是：[58.62.92.104] 来自：广东省广州市 电信

http://www.goubanjia.com/
 全网代理IP
120.234.63.196:3128 	透明 	https 	中国   广东   深圳 	移动 	0.366 秒 	18分钟前 	18天
"""
#! -*- coding:utf8 -*-
import  urllib.request
import  sys
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

## 设置代理ip
proxy = urllib.request.ProxyHandler(
    {'http':'120.234.63.196:3128'})

 # 获取一个opener对象
opener = urllib.request.build_opener(proxy)

  # 给opener添加请求头，使用的是元组的方式
opener.addheaders = [('User-Agent',
      "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0")]

urllib.request.install_opener(opener)

response = opener.open('http://2019.ip138.com/ic.asp').read()

print(response, end='\n-------------------\n')
#b'<html>\r\n<head>\r\n<meta http-equiv="content-type" content="text/html; charset=gb2312">\r\n<title> \xc4\xfa\xb5\xc4IP\xb5\xd8\xd6\xb7 </title>\r\n</head>\r\n<body style="margin:0px"><center>\xc4\xfa\xb5\xc4IP\xca\xc7\xa3\xba[58.62.92.104] \xc0\xb4\xd7\xd4\xa3\xba\xb9\xe3\xb6\xab\xca\xa1\xb9\xe3\xd6\xdd\xca\xd0 \xb5\xe7\xd0\xc5</center></body></html>'

page = response.decode('gb18030')
print(page)
#<html>
#<head>
#<meta http-equiv="content-type" content="text/html; charset=gb2312">
#<title> 您的IP地址 </title>
#</head>
#<body style="margin:0px"><center>您的IP是：[58.62.92.104] 来自：广东省广州市 电信</center></body></html>



if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)




#!/usr/bin/env  python3
#coding:UTF-8
#! -*- coding:utf8 -*-
"""#coding=UTF-8
[root@room9pc01 spider]# ls  /usr/local/lib/python3.6/site-packages/requests/
adapters.py  compat.py      hooks.py            packages.py      structures.py
api.py       cookies.py     __init__.py         __pycache__      utils.py
auth.py      exceptions.py  _internal_utils.py  sessions.py      __version__.py
certs.py     help.py        models.py           status_codes.py

# tail   -1  /var/log/httpd/access_log
192.168.0.254 - - [06/May/2019:14:44:15 +0800] "GET /favicon.ico HTTP/1.1" 404 209 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
>>> strx = '中文abc'
>>> type(strx)
<class 'str'>

>>> byteX = strx.encode('gb18030')

>>> type(byteX)
<class 'bytes'>
>>> byteX
b'\xd6\xd0\xce\xc4abc'

>>> decodeStrx = byteX.decode('gb18030')

>>> decodeStrx
'中文abc'
>>> type(decodeStrx)
<class 'str'>
>>> 
>>>
>>> strx2 = '中文啊abc'
>>> type(strx2)
<class 'str'>

>>> byteX2 = strx2.encode('utf8')

>>> type(byteX2)
<class 'bytes'>
>>> byteX2
b'\xe4\xb8\xad\xe6\x96\x87\xe5\x95\x8aabc'

>>> decodeStrx2 = byteX2.decode('utf8')

>>> decodeStrx2
'中文啊abc'
>>> type(decodeStrx2)
<class 'str'>
>>> 

postdata = urllib.parse.urlencode(data).encode('utf-8')

response = opener.open('http://2019.ip138.com/ic.asp').read()

page = response.decode('gb18030')

quote      英 [kwəʊt] 
     v.引用;引述;举例说明;开价;出价;报价
     n.引用
parameter       英 [pəˈræmɪtə(r)]
       n.决定因素;规范;范围

>>> import   urllib.request

>>> urllib.request.quote('hello中文')
'hello%E4%B8%AD%E6%96%87'
>>> urllib.request.unquote('hello%E4%B8%AD%E6%96%87')
'hello中文'

>>> urllib.request.quote('中')
'%E4%B8%AD'
>>> urllib.request.unquote('%E4%B8%AD')
'中'
>>> 
"""
import  urllib.request
import  urllib.error
import  urllib.parse
import  sys
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

def  download(url, fname):
  header = {
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
  }
  request = urllib.request.Request(url,headers=header)
  html = urllib.request.urlopen(request)
  with  open(fname, 'wb') as  fobj:
    while True:
      data = html.read(1024)
      if  not data:
        break
      fobj.write(data)

print('================================\n')

header = {
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
  }
url = 'http://127.0.0.1/abc/'
request = urllib.request.Request(url,headers=header)

try:
  html = urllib.request.urlopen(request)
except urllib.error.HTTPError  as  HEr:
  print('\n----- urllib.error.HTTPError: ', HEr, end='\n\n')
#----- urllib.error.HTTPError:  HTTP Error 404: Not Found


#[root@room9pc01 urllib_paramiko]# chmod  770  /var/www/html/zidir/index.html
#[root@room9pc01 urllib_paramiko]# ls  -ld  /var/www/html/zidir/
#drwxr-xr-x 2 root root 4096 5月   6 17:14 /var/www/html/zidir/
#
#[root@room9pc01 urllib_paramiko]# ll  /var/www/html/zidir/index.html 
#-rwxrwx--- 1 root root 18 5月   6 17:14 /var/www/html/zidir/index.html
#
#[root@room9pc01 urllib_paramiko]# elinks  -dump  http://127.0.0.1/zidir
#                                   Forbidden
#
#   You don't have permission to access /zidir/index.html on this server.


url = 'http://127.0.0.1/zidir'
request = urllib.request.Request(url,headers=header)
try:
  html = urllib.request.urlopen(request)
except urllib.error.HTTPError  as  HEr:
  print('\n-------------- error.HTTPError: ', HEr, end='\n\n')
#-------------- error.HTTPError:  HTTP Error 403: Forbidden



if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)
#  download('https://www.baidu.com/s?ie=utf-8&wd=%E5%B0%A4%E6%9E%9C%E7%BD%91%E8%AF%B1%E6%83%91%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87%E5%A4%A7%E5%85%A8', './Test/baidutest.html')

#  download('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1557135913238&di=08b32ae9b1af2bbf514acbf6327e6a10&imgtype=0&src=http%3A%2F%2F00.minipic.eastday.com%2F20170413%2F20170413200739_cacbbcf55ced4150d07aecf717847681_1.jpeg', './Test/test.jpg')

#  download('https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1201304369,1657169105&fm=26&gp=0.jpg', './Test/x1.jpg')

  download('http://127.0.0.1/zidir/test.jpg', './Test/x2.jpg')






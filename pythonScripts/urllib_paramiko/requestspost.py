#!/usr/bin/env  python3
#coding:UTF-8
#! -*- coding:utf8 -*-
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

parameter       英 [pəˈræmɪtə(r)]
       n.决定因素;规范;范围
"""
import  requests
import  sys
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

url = "http://192.168.0.254:8888/login"
data = {'username':'abc','password':'abc'}

resp = requests.post(url,data=data)
print(resp.text)
#{"code": 0, "msg": "OK HAHAhaha ---ok"}


header = {
 'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
 'Rerferer':'http://www.baidu.com'
}
#data = {'username':'admin','password':'admin'}
#postdata = urllib.parse.urlencode(data).encode('utf-8')
#request = urllib.request.Request(url,data=postdata, headers=header)
#response = urllib.request.urlopen(request).read()

response = requests.get("http://www.goubanjia.com",
                    headers=header)
print(response,end = '\n----------------\n')
#<Response [200]>
#注意如果没有 headers 则返回<Response [403]>


resp = requests.get("http://www.goubanjia.com",
                    headers=header, proxies={})
print(resp)
#<Response [200]>

proxies = {
 "http" :"120.234.63.196:3128",
 "http" :"121.8.98.196:80",
 "http" :"202.112.237.102:3128"
}
resp2 = requests.get("http://2019.ip138.com/ic.asp",
                    headers=header, proxies=proxies)
print(resp2, end='\n----------resp2\n')
#<Response [200]>

resp3 = requests.get("http://example.org/",
                    headers=header, proxies=proxies)
print(resp3, end='\n----------resp3\n')
#<Response [200]>


if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)



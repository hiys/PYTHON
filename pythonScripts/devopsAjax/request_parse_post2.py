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
"""
#! -*- coding: utf8 -*-

import urllib.request
import urllib.parse
import  sys
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

url = "http://192.168.0.254:8888/login"
header = {
 'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
}
# 192.168.0.254:8888/login  物理机IP
data = {'username':'admin','password':'12345'}
postdata = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url,data=postdata, headers=header)

response = urllib.request.urlopen(request).read()

print(response, end ='\n-------1---------\n')

response = urllib.request.urlopen("http://192.168.0.254:8888/").read()
print(response, end ='\n-------2---------\n')


if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)



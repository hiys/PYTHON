#!/usr/bin/env  python3
#coding:UTF-8
#! -*- coding:utf8 -*-
"""#coding=UTF-8
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

s = requests.Session()

s.post(url,data=data)
resp = s.get("http://192.168.0.254:8888/")
print(resp.text, end='\n-----------resp-----------\n')
#Hello, world







if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)



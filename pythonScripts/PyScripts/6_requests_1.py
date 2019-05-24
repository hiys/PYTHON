#! -*- coding:utf8 -*-
import requests

payload = {'key1':'value1',
           'key2':['v1','v2'],
           'wd':'国家食品药品监督管理局'
           }

r = requests.get("http://httpbin.org/get",params=payload)
obj = r.json()
print(r.json())
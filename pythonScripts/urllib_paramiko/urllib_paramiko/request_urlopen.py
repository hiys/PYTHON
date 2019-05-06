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
import  urllib.request
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


if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)
  download('https://www.baidu.com/s?ie=utf-8&wd=%E5%B0%A4%E6%9E%9C%E7%BD%91%E8%AF%B1%E6%83%91%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87%E5%A4%A7%E5%85%A8', './Test/baidutest.html')

  download('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1557135913238&di=08b32ae9b1af2bbf514acbf6327e6a10&imgtype=0&src=http%3A%2F%2F00.minipic.eastday.com%2F20170413%2F20170413200739_cacbbcf55ced4150d07aecf717847681_1.jpeg', './Test/test.jpg')

  download('https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1201304369,1657169105&fm=26&gp=0.jpg', './Test/x1.jpg')






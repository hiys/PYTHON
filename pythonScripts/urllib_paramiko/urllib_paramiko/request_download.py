#!/usr/bin/env  python3
#coding:UTF-8
#! -*- coding:utf8 -*-
"""#coding=UTF-8

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

pattern        美 [ˈpætərn]  
    n.模式;方式;范例;典范;榜样;样板;图案;花样;式样
    v.构成图案(或花样);

>>> import   urllib.request

>>> urllib.request.quote('hello中文')
'hello%E4%B8%AD%E6%96%87'
>>> urllib.request.unquote('hello%E4%B8%AD%E6%96%87')
'hello中文'

>>> urllib.request.quote('中')
'%E4%B8%AD'
>>> urllib.request.unquote('%E4%B8%AD')
'中'
>>> url = 'http://127.0.0.1/zidir/test.jpg'
>>> url.split('/')
['http:', '', '127.0.0.1', 'zidir', 'test.jpg']
>>> url.split('/')[-1]
'test.jpg'
>>> 
>>> 
"""
import  urllib.request
import  urllib.error
import  urllib.parse
import  sys, re, os

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

print('============= download(url, fname) ===================\n')

def  search_url(fname, patt):
  cpatt = re.compile(patt) #编译正则表达式模式，返回一个对象。
  resultlist = []  # 把所有的匹配存入该列表
  with  open(fname) as fobj:  # 打开文件时，可以指定字符集
    for line  in  fobj:
      #对整个字符串进行搜索匹配，返回第一个匹配的字符串的 match 对象
#<img src="http://i1.whymtj.com/uploads/tu/201608/206/c47.jpg" height="165" width="220">
      match_objs = cpatt.search(line) # 找到一行中的多个模式
      for  m  in  match_objs:
        if m :
          resultlist.append(m.group())   # 将找到的内容追加到列表
  return  resultlist


print('============ search_url(fname, patt) ====================\n')

#url="http://i1.whymtj.com/uploads/tu/201608/206/c47.jpg"
def  urlimg(imglist, img_dir):
  for url  in  img_list:
    fname = url.split('/')[-1]   # 取出网址中的文件名
    fname = os.path.join(img_dir, fname) # 拼接本地文件绝对路径
    try:
      download(url, fname)
    except  urllib.error.HTTPError as he:
      print('\n------------- error url= ',url, he, sep='\n')

print('==============  urlimg(imglist, img_dir) ==================\n')


if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)

  img_dir = '/root/urllib_paramiko/Test/imgs'
  if not os.path.exists(img_dir):
    os.mkdir(img_dir)

  download('http://127.0.0.1/', './Test/down.html')
  download('http://www.umei.cc/meinvtupian/xingganmeinv/185526_4.htm', './Test/down1.html')
  download('http://www.umei.cc/meinvtupian/xingganmeinv/185526_5.htm', './Test/down2.html')
  download('http://www.umei.cc/meinvtupian/meinvxiezhen/', './Test/down3.html')
  download('http://www.umei.cc/meinvtupian/xingganmeinv/', './Test/down4.html')

  img_pattern = 'http://[\w./-]+\.(jpg|jpeg|gif|png)'  # 编写图片url的正则表达式

  img_list = search_url('/root/urllib_paramiko/Test/down.html', img_pattern)
#  img_list2 = search_url('/root/urllib_paramiko/Test/down2.html', img_pattern)
#  img_list3 = search_url('/root/urllib_paramiko/Test/down3.html', img_pattern)
#  img_list4 = search_url('/root/urllib_paramiko/Test/down4.html', img_pattern)

#  urlimg(imglist, img_dir)
#  urlimg(imglist2, img_dir)
#  urlimg(imglist3, img_dir)
#  urlimg(imglist4, img_dir)
  
    


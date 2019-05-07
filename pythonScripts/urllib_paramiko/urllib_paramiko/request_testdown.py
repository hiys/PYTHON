#!/usr/bin/env  python3
#coding:UTF-8
#! -*- coding:utf8 -*-
"""#coding=UTF-8
"""
import  urllib.request
import  urllib.error
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
      if match_objs:
        resultlist.append(match_objs.group())   # 将找到的内容追加到列表
  return  resultlist


print('============ search_url(fname, patt) ====================\n')

#url="http://i1.whymtj.com/uploads/tu/201608/206/c47.jpg"
def  urlimg(imglist, img_dir):
  for url  in  imglist:
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

  img_pattern = 'http://[\w./-]+\.(jpg|jpeg|gif|png)'  # 编写图片url的正则表达式

  img_list = search_url('/root/urllib_paramiko/Test/down.html', img_pattern)

  urlimg(img_list, img_dir)
  
    


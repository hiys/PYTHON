#! /usr/bin/env python3
#coding:UTF-8
"""这是测试模版说明--------
 * 表示把序列对象（列表，字符串，元组等） 拆开，得到个体"""
import  sys, os

print(sys.path)
#['/root/pyscripts/day07/zidir', '/usr/local/lib/python36.zip', '/usr/local/lib/python3.6', '/usr/local/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages']

print('os.path.dirname(os.path.abspath(__file__)) is  %s' % os.path.dirname(os.path.abspath(__file__) ))
#os.path.dirname(os.path.abspath(__file__)) is  /root/pyscripts/day07/zidir

print('__file__  is  %s' % __file__)
#__file__  is  zifile.py

print('os.path.abspath(__file__) is   %s' % os.path.abspath(__file__)) #绝对路径abspath
#os.path.abspath(__file__) is   /root/pyscripts/day07/zidir/zifile.py

sys.path.append('..')
print(sys.path)
#['/root/pyscripts/day07/zidir', '/usr/local/lib/python36.zip', '/usr/local/lib/python3.6', '/usr/local/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages', '..']

import  mobantest
#__name__  is mobantest

print('mobantest.__file__  is %s' % mobantest.__file__)
#mobantest.__file__  is ../mobantest.py


print('\033[31;47;1m zifile --- __name__  is %s\033[0m' %  __name__)
# zifile --- __name__  is __main__


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv  is %s\033[0m\n' % sys.argv) 

  print(mobantest.date)
  #2019年*04月*11日 11时:09分:35秒

  infolist = [ 2233, True ,'zifile']
  mobantest.get_abc(*infolist)
  # A is 2233	B is True	 C is zifile



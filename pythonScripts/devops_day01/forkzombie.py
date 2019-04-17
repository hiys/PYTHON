#!/usr/bin/env  python3
"""#coding=UTF-8
"""

import	 sys, os, time

def  invoke():
  date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())
  return   '%s\n-------**** %f' %  (date, time.time())

print('\033[31;40;1m__name__  is %s\n\033[0m' % __name__)

os.fork()

print(invoke())




  

if __name__ == '__main__':

  print('\033[30;43;1m sys.argv[0]  is %s \033[0m' % sys.argv[0])







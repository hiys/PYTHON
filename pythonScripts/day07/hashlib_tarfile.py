#! /usr/bin/env python3
#coding:UTF-8
"""这是模版说明--------
•  hashlib用来替换md5和sha模块,并使他们的API一致,
专门提供hash算法
•  包括md5、sha1、sha224、sha256、sha384、sha512
•  tarfile模块允许创建、访问tar文件
•  同时支持gzip、bzip2格式"""

import  sys, os, hashlib,  tarfile

#print(sys.path)
#print('os.path.dirname(os.path.abspath(__file__)) is  %s' % os.path.dirname(os.path.abspath(__file__) ))  #当前文件的父目录

#print('__file__  is  %s' % __file__)   #相对路径

#print('os.path.abspath(__file__) is  %s' % os.path.abspath(__file__)) #绝对路径abspath

#sys.path.append('..')

def  testhashlib():
  hello = bytes('hello boy',encoding='utf8')
  m = hashlib.md5(hello)
  print(m.hexdigest)     #输出函数对象名信息
  #<built-in method hexdigest of _hashlib.HASH object at 0x7f03315607d8>
  
  print(m.hexdigest(),end = '\n-----------\n')  #输出16进制数字
  #03f80b5b465c40e0591830c1d3c970e5

#[root@V0 day07]# md5sum  /root/pyscripts/day07/filetest.py   zidir/zifile.py 
#7a358b09af7c8553e8295ca271d0529b  /root/pyscripts/day07/filetest.py
#7a358b09af7c8553e8295ca271d0529b  zidir/zifile.py
#[root@V0 day07]# 
  
  with  open('/root/pyscripts/day07/filetest.py', 'rb') as fobj:
    data = fobj.read()
  mdata = hashlib.md5( data )
  print(mdata.hexdigest())
  #7a358b09af7c8553e8295ca271d0529b

  print(type(mdata.hexdigest()))
  #<class 'str'>
  print('\n----------testhashlib----------\n')


def  check_md5(fname):
  m = hashlib.md5()  #生成md5值类型的对象
  print(type(m))
  #<class '_hashlib.HASH'>

  print('m  is ---  %s' % m)
  #m  is ---  <md5 HASH object @ 0x7f4007b5d918>

  count = 0
  with open(fname, 'rb') as  fobj:
    while True:
      data2 = fobj.read(1024) #默认内存以Byte 字节为单位(1byte = 8bit)
      if not data2:
        break
      m.update(data2)  #更新md5值数据    
      count += 1
  print('一共循环读取了 %d 次' % count)
  #一共循环读取了 2 次
  return  m.hexdigest()


def  testarfile():

#[root@V0 day07]# ls  -lh   /root/pyscripts/day07/zidir/zifile.py
#-rw-r--r-- 1 root root 1.5K 4月  11 11:16 /root/pyscripts/day07/zidir/zifile.py
#[root@V0 day07]# ls  /root/pyscripts/day07/zidir/
#zifile.py
#[root@V0 day07]# ls  -lh   /root/pyscripts/day07/filetest.py 
#-rw-r--r-- 1 root root 1.5K 4月  11 11:42 /root/pyscripts/day07/filetest.py
#[root@V0 day07]# ls  /root/pyscripts/day07/newtarx.tar.gz
#ls: 无法访问/root/pyscripts/day07/newtarx.tar.gz: 没有那个文件或目录
#[root@V0 day07]#


##以gzip的压缩格式,在目录/root/pyscripts/day07/下打开新建压缩包newtarx.tar.gz

  tar = tarfile.open('/root/pyscripts/day07/newtarx.tar.gz', 'w:gz') #以 gzip的压缩格式,  打开新建的压缩包newtarx.tar.gz

  tar.add('/root/pyscripts/day07/zidir/zifile.py') #将要被压缩的文件
  tar.add('/root/pyscripts/day07/filetest.py')
  tar.close()

#产生了新压缩文件 day07/newtarx.tar.gz

#[root@V0 day07]# ll  /root/pyscripts/day07/newtarx.tar.gz
#-rw-r--r-- 1 root root 802 4月  11 13:54 /root/pyscripts/day07/newtarx.tar.gz
#[root@V0 day07]# du  -sh   /root/pyscripts/day07/newtarx.tar.gz
#4.0K	/root/pyscripts/day07/newtarx.tar.gz
#[root@V0 day07]# tar  -tzPf  /root/pyscripts/day07/newtarx.tar.gz
#root/pyscripts/day07/zidir/zifile.py
#root/pyscripts/day07/filetest.py




if __name__ == '__main__':
  print('\033[30;43;1m sys.argv  is %s\033[0m\n' % sys.argv) 
#  testhashlib()

#  print('\n--------~~~~---------\n')
  #--------~~~~---------
#[root@V0 day07]# ll  /root/pyscripts/day07/filetest.py
#-rw-r--r-- 1 root root 1505 4月  11 11:42 /root/pyscripts/day07/filetest.py
#  print(check_md5('/root/pyscripts/day07/filetest.py') )
  #7a358b09af7c8553e8295ca271d0529b

  testarfile()



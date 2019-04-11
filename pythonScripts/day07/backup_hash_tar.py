#! /usr/bin/env python3
#coding:UTF-8
"""这是模版说明--------
•  hashlib用来替换md5和sha模块,并使他们的API一致,
专门提供hash算法
•  包括md5、sha1、sha224、sha256、sha384、sha512
•  tarfile模块允许创建、访问tar文件
•  同时支持gzip、bzip2格式
>>> import   os
>>> os.path.basename('/root/pyscripts/day07/filetest.py')
'filetest.py'
>>> 
>>> os.path.dirname('/root/pyscripts/day07/filetest.py')
'/root/pyscripts/day07'
>>>
>>> os.path.abspath('/root/pyscripts/day07/filetest.py')
'/root/pyscripts/day07/filetest.py'
>>> import  time
>>> time.strftime('%m月%d日%H时%M分%S秒')
'04月11日17时13分19秒'
>>> """

import  sys, os, hashlib,  tarfile, time
import  pickle 

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




def  full_backup(src_dir, dst_dir, md5file):
  """tarfname 将要备份的新产生的压缩包 """

  print('------- 00000000 -------')
  tarfname = os.path.basename(src_dir.rstrip('/'))
  print('tarfname is  %s ---- 1 -----' %  tarfname)

  tarfname = '%s_full_%s.tar.gz' % (tarfname, time.strftime('%m月%d日%H时%M分%S秒'))
  print('tarfname is  %s ---------- 2 --------' %  tarfname)

  tarfname = os.path.join(dst_dir, tarfname)  #拼接文件名全称
  print('tarfname is  %s ---------- 3 --------' %  tarfname)
 
  print(os.listdir(src_dir),end = '\n\n')

#>>> fname
#'/root/pyscripts/day07/srctest'
#>>> os.listdir(fname)
#['filetest.py', 'zifile.py', 'zisrcdir']
#>>> os.listdir(fname)[0]
#'filetest.py'
#>>> os.listdir(fname)[1]
#'zifile.py'
#>>> os.listdir(fname)[-1]
#'zisrcdir'
#>>> 
#>>> zidir = os.path.join( fname,  os.listdir(fname)[-1])
#>>> zidir
#'/root/pyscripts/day07/srctest/zisrcdir'
#>>> os.listdir(zidir)
#['zisrcfile.py']
#>>> 

  src_file = os.path.join(src_dir,  os.listdir(src_dir)[0])
  src_file2 = os.path.join(src_dir, os.listdir(src_dir)[1])
  print('src_file  is %s  exists %s \n src_file2 is %s  exists  %s\n' %  \
  (src_file, os.path.exists(src_file), src_file2, os.path.exists(src_file2)))


  tar = tarfile.open(tarfname, 'w:gz') #以gzip的压缩格式,打开新建的压缩包tarfname
#  tar.add(src_file)   #将要被压缩的文件
#  tar.add(src_file2)  #将要被压缩的文件
  tar.add(src_dir)   #直接把目录下的所有文件压缩成一个压缩包(名为tarfname)
  tar.close()

#>>> for  path,  dirs, files  in  os.walk(fname):
#...   for  each_file  in  files:
#...     print(os.path.join(path, each_file))
#... 
#/root/pyscripts/day07/srctest/filetest.py
#/root/pyscripts/day07/srctest/zifile.py
#/root/pyscripts/day07/srctest/zisrcdir/zisrcfile.py
#>>> 
#
#>>> import   hashlib
#>>> with  open('/root/pyscripts/day07/filetest.py', 'rb') as fobj:
#...   data = fobj.read()
#... 
#>>> mdata = hashlib.md5( data )
#
#>>> print(type(mdata))
#<class '_hashlib.HASH'>
#
#>>> print(type(mdata.hexdigest()))
#<class 'str'>
#
#>>> print(mdata.hexdigest())
#7a358b09af7c8553e8295ca271d0529b
#
#>>> print(mdata)
#<md5 HASH object @ 0x7fb28998fa08>
#>>> 


  md5dict = {}  #设置文件全称名是键key : value值 是md5 计算出来的字符串值

  for  rootpath,  folders, files in  os.walk(src_dir):
    for  each_file  in  files:
      print(os.path.join(rootpath, each_file))
      key = os.path.join(rootpath, each_file)
      md5dict[key] = check_md5(key)
  print(md5dict,end = '\n ----- md5dict ------\n')

  #新建文件md5file = rootdir+'zidir/md5.data'保存字典{文件名:md5值16进制字符串}

  with  open(md5file, 'wb') as  fobj: #新建一个文件保存字典md5dict{}
    pickle.dump(md5dict, fobj)



def  increase_backup(src_dir, dst_dir, md5file):
  "increase  增加，增大，增多"
  print('------- 11111111 -------')

  tarfname = os.path.basename(src_dir.rstrip('/'))
  print('tarfname is  %s ---- 1 -----' %  tarfname)

  tarfname = '%s__increase__%s.tar.gz' % (tarfname, time.strftime('%m月%d日%H时%M分%S秒'))
  print('tarfname is  %s ---------- 2 --------' %  tarfname)

  tarfname = os.path.join(dst_dir, tarfname)  #拼接文件名全称
  print('tarfname is  %s ---------- 3 --------' %  tarfname)

  new_md5dict = {}

  with open(md5file, 'rb')  as  fobj:
    oldmd5 = pickle.load(fobj)



if __name__ == '__main__':
  print('\033[30;43;1m sys.argv  is %s\033[0m\n' % sys.argv) 
  
  rootdir = '/root/pyscripts/day07/'
  if os.path.exists(rootdir):
    print('The root directory  already  exists -----')

  src_dir = rootdir + 'srctest/'
  if  os.path.exists(src_dir):
    print('The src_dir directory  already  exists -----')
    print(os.path.abspath(src_dir),end = '\n\n')

  dst_dir = rootdir + 'dstBackupDir/'
  md5file = rootdir + 'zidir/md5.data'

#[root@V0 day07]# rm  -rf  zidir/   dstBackupDir/
#[root@V0 day07]# ls    dstBackupDir/   zidir/
#ls: 无法访问dstBackupDir/: 没有那个文件或目录
#ls: 无法访问zidir/: 没有那个文件或目录

  if not os.path.exists(dst_dir):
    os.mkdir(dst_dir)
  else:
    print(os.path.abspath(dst_dir), end = '\n--- dst_dir ---\n')
    #/root/pyscripts/day07/dstBackupDir
    #--- dst_dir ---

  if not  os.path.exists('/root/pyscripts/day07/zidir'):
    os.mkdir('/root/pyscripts/day07/zidir/')
  else:
    print(os.path.dirname('/root/pyscripts/day07/zidir'), end = '\n\n')
    #/root/pyscripts/day07

#[root@V0 day07]# ls  -ld    dstBackupDir/   zidir/
#drwxr-xr-x 2 root root 6 4月  11 16:35 dstBackupDir/
#drwxr-xr-x 2 root root 6 4月  11 16:35 zidir/



  if  int(time.strftime('%S',time.localtime())) % 3 == 0 :
    full_backup(src_dir, dst_dir, md5file)

  elif int(time.strftime('%S',time.localtime())) % 3 == 1:
    increase_backup(src_dir, dst_dir, md5file)

  else:
    print('This time is 222222222 ---%S---')





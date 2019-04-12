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
import  pickle, shutil

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

#  src_file = os.path.join(src_dir,  os.listdir(src_dir)[0])
#  src_file2 = os.path.join(src_dir, os.listdir(src_dir)[1])
#  print('src_file  is %s  exists %s \n src_file2 is %s  exists  %s\n' %  \
#  (src_file, os.path.exists(src_file), src_file2, os.path.exists(src_file2)))


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


  #新建文件md5file = dst_dir + 'md5.data'保存字典{文件名:md5值16进制字符串}

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

  new_md5dict = {} #设置文件全称名是键key : value值 是md5 计算出来的字符串>值

  with open(md5file, 'rb')  as  fobj: #打开旧文件md5file读取旧字典oldmd5dict{}
    oldmd5dict = pickle.load(fobj)  #旧字典暂时保存在内存中

  for  rootpath,  folders, files in  os.walk(src_dir):
    for  each_file  in  files:
      print(os.path.join(rootpath, each_file))
      key = os.path.join(rootpath, each_file)
      new_md5dict[key] = check_md5(key)

  print(new_md5dict,end = '\n ----- new_md5dict ------\n')

  #新建文件md5file = dst_dir + 'md5.data'保存字典{文件名:md5值16进制字符串}

  with  open(md5file, 'wb') as  fobj: #重新新建文件保存新字典new_md5dict{}
    pickle.dump(new_md5dict, fobj)  #新字典直接保存在硬盘文件md5file 中


  increase_fileslist = []

  for  key  in  new_md5dict:
#    if key  not in oldmd5dict:
#      tar.add(key)   #把新字典new_md5dict的key中对应的新增文件压缩保存在压缩包tarfname中
#    elif new_md5dict[key] != oldmd5dict[key]:
#      tar.add(key) #把新字典new_md5dict中有过改动的旧文件保存在压缩包tarfname中
   ##把新字典new_md5dict的key中对应的新添加的文件 和 有过改动的旧文件 压缩保存在压缩包tarfname中
    if oldmd5dict.get(key) != new_md5dict[key]:
   #   tar.add(key)
      increase_fileslist.append(key)
      print('新加入压缩列表increase_fileslist[]的文件是 %s ---\n' %  key)
    else:
      print('\n 没有任何变化!\n')


  if  len(increase_fileslist) == 0:
    print('\n没有任何变化,不进行increase_backup(src_dir, dst_dir, md5file)压缩!\n')
  else:   
    print('\n=========== tarfile.open(tarfname, "w:gz") ================\n')
    tar = tarfile.open(tarfname, 'w:gz') 
    #以gzip的压缩格式,打开新建的压缩包tarfname

#>>> type(len(listx))
#<class 'int'>
#>>> listx = ['11',22]
#>>> listx.append('222')
#>>> listx
#['11', 22, '222']
#>>> 
#>>> for i in  listx:
#...   print(listx.index(i), i, sep = ' --- ')
#... 
#0 --- 11
#1 --- 22
#2 --- 222
#>>>
    ##把新字典new_md5dict的key中对应的新添加的文件 和 有过改动的旧文件 压缩保存在压>缩包tarfname中
    for  file  in  increase_fileslist:
      tar.add(file)
      print('新加的将要压缩的文件是 %s ---\n' %  file)
    tar.close()
    print('\n------------tar.close() -----------------\n')



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
  md5file = dst_dir + 'md5.data'


#[root@V0 day07]# ls  srctest/
#filetest.py  zifile.py  zisrcdir
#[root@V0 day07]# ls  srctest/zisrcdir/
#zisrcfile.py
#[root@V0 day07]# rm  -f  srctest/*秒.py
#[root@V0 day07]# rm  -rf    dstBackupDir/
#[root@V0 day07]# ls  dstBackupDir/
#ls: 无法访问dstBackupDir/: 没有那个文件或目录

  if not os.path.exists(dst_dir):
    os.mkdir(dst_dir)
  else:
    print(os.path.abspath(dst_dir), end = '\n--- dst_dir ---\n')
    #/root/pyscripts/day07/dstBackupDir
    #--- dst_dir ---

    print(os.path.dirname(md5file), end = '\n\n')
    #/root/pyscripts/day07/dstBackupDir

#[root@V0 day07]# ls   dstBackupDir/
#md5.data  srctest_full_04月12日11时03分57秒.tar.gz
#[root@V0 day07]# du  -sh   dstBackupDir/srctest_full_04月12日11时03分57秒.tar.gz 
#4.0K	dstBackupDir/srctest_full_04月12日11时03分57秒.tar.gz




  if  int(time.strftime('%S',time.localtime())) % 3 == 0 :
    full_backup(src_dir, dst_dir, md5file)

  elif int(time.strftime('%S',time.localtime())) % 3 == 1:
    increase_backup(src_dir, dst_dir, md5file)

  else:
    src_file = os.path.join(src_dir,  os.listdir(src_dir)[0])
    print('src_file  is %s  exists %s \n' %  \
        (src_file, os.path.exists(src_file)))
    dst_newcopy_file = '%s_newcopy_%s.py' % (src_file.rstrip('.py'), time.strftime('%m月%d日%H时%M分%S秒'))
    print('dst_newcopy_file is  %s -----------------' %  dst_newcopy_file)

    with open(src_file) as  src_fobj:
      with open(dst_newcopy_file, 'w') as  dst_fobj:
        shutil.copyfileobj(src_fobj, dst_fobj)
    print('dst_newcopy_file  is %s  exists %s \n' %  \
     (dst_newcopy_file,  os.path.exists(dst_newcopy_file)))

    print('This time is 222222222 ---%S---')
    




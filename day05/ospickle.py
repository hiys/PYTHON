#!/usr/bin/env  python3
import  sys, os, pickle
print('\033[31;47;1m__name__ is %s\033[0m' % __name__)

def  ostest():

  if  os.path.exists('/osdir'):
    if os.path.exists('/osdir/copyhosts'):
      os.remove('/osdir/copyhosts') #删除绝对路径下的文件copyhosts
    os.removedirs('/osdir')   ## 递归删除没有文件的空目录
  os.mkdir('/osdir')  #创建目录

  print(os.listdir('/osdir')) #查看目录,列出指定目录的文件

  os.symlink('/etc/hosts', '/osdir/copyhosts') 
#创建符号链接(即软链接),并且改写文件链接名

  print(os.listdir('/osdir')) #查看目录,列出指定目录的文件

  os.chdir('/osdir')   #切换改变工作目录,等同shell中的 cd 命令

  print(os.getcwd())  #查看当前工作目录的路径



if __name__ == '__main__':
  print('\033[30;43;1msys.argv is %s\033[0m' % sys.argv)
  ostest()



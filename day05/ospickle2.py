#!/usr/bin/env   python3
import  sys, os, pickle
print('\033[31;47;1m__name__ is %s\033[0m' % __name__)

#sys.argv[1] = '/root/桌面/Test/newzidyi.data'
# fpathname = sys.argv[1]
def  ospickletest(fpathname):
  if os.path.exists(fpathname):
    os.remove(fpathname)
  
  fwObj = open(fpathname, 'wb')
  print('新建以"wb"方式打开的文件，返回 类文件对象 %s' % type(fwObj))
  print('\n文件%s 刚开始的大小是 %d \n' %  (fpathname, os.stat(fpathname).st_size))
  print('当前目录 %s 下的所有文件是 ----\n%s'\
   %  ( os.path.dirname(fpathname),os.listdir(os.path.dirname(fpathname))))

  shoplist = ['apple','mango','carrot','eggs']
  print('\n正在序列化对象----dump(shoplist,fwObj),\
  \n将列表对象shoplist保存到文件%s 中-----' % fpathname)

  pickle.dump(shoplist,fwObj)
  fwObj.close()   #关闭写入流

  print('\n文件%s 存储了\n列表对象 %s 后的大小是  %d \n' \
  %  (fpathname,shoplist,os.stat(fpathname).st_size))

  print('正在打开文件---\n%s-----' %  fpathname)
  frbObj = open(fpathname, 'rb')
  print('\n以"rb"方式打开已经存在的文件，返回 类文件对象 %s' % type(frbObj))

  print('正在反序列化对象----load(frbObj),\
  \n从文件%s 中\n将数据解析为一个python对象（比如是列表对象)-----' % fpathname)

  readobj = pickle.load(frbObj)

  print("\n解析出来的python对象是\n%s\n对象类型是%s" % (readobj,type(readobj)))
  frbObj.close()  
  print('第一个数据是 %s  最后一个数据是 %s' % (readobj[0],readobj[-1]))


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv is %s \033[0m' % sys.argv)
  print('\033[32;46;1m sys.argv[1]  is %s \033[0m' % sys.argv[1])
  ospickletest(sys.argv[1])


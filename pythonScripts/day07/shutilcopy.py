#!/usr/bin/env   python3
import  shutil, sys, time, datetime
sys.stdout.write("\033[31;1m __name__  red-is  %s \n\033[0m" % __name__)

#时间模块  time.time()函数
localt = time.localtime()
#print('local time is %s  type is  %s ' % (localt,type(localt)))

#将元组的时间格式转换成字符串格式的时间
#print('LocalTime is %s ' % time.strftime('%Y-%m-%d %H:%M:%S',localt))

sys.stdout.write('\033[30;43;1mDatetime now is %s yellow\n\033[0m' % datetime.datetime.now())
def  copyx(srcrb = 'filex.txt',dstwb = 'filecopy.txt'):
  start = time.time()
  with open(srcrb) as src_fobj:
    with open(dstwb,'w') as dst_fobj:
      shutil.copyfileobj(src_fobj,dst_fobj) 
#注意"类似文件的对象"和"文件"的区别.copyfile(src_f,dst_f)
  end = time.time()
  print("\033[32;40;1m The runningtime green-is  %f  seconds\033[0m" % (end - start))
  src_f = 'filey.txt'
  dst_f = 'filey2.txt'
#注意"类似文件的对象"和"文件"的区别.copyfile(src_f,dst_f)
  shutil.copyfile(src_f,dst_f) 

#将权限位从'filex.txt'复制到'filemode.txt'。
#文件内容,所有者和组不受影响。windows 不支持
#  shutil.copymode('filex.txt','filemode.txt')

#将权限位,最后访问时间,上次修改时间和标志
#从src  复制到 dst。
#  shutil.copystat('filex.txt','filestat.txt')

#将文件src复制到文件或目录dst
#src和dst应为字符串。
#如果dst指定目录,
#则文件将使用src的基本文件名复制到dst中。
#返回新创建的文件的路径。
#注意与 shutil.copyfile(src_f,dst_f) 的区别
#  shutil.copy('filex.txt','newdir/')
#  shutil.copy('filex.txt','newdir/fx.txt')

#相当于 cp -p
#  shutil.copy2('filey.txt','newdir')

#递归地复制以src为根的整个目录树,返回目标目录。
#由dst命名的目标目录不能已经存在。
#  shutil.copytree('newdir/', '/root/zidyidir')

#删除整个目录树
#  shutil.rmtree('/root/zidyidir')

#递归地 将 文件 或 目录 (src) 移动到
#另一个位置(dst),并返回目标。
#  shutil.move('filestat.txt', 'newdir/')

#更改给定路径的所有者用户 和/或 组
  shutil.chown('newdir/fx.txt','lisi','lisi')



if __name__ == '__main__':
  print(sys.argv)
  copyx(sys.argv[1],sys.argv[2])


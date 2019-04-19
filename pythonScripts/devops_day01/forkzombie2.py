#!/usr/bin/env  python3
"""#coding=UTF-8
"""
import	 sys, os, time
def  invoke():
  date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())
  return   '%s\n-------**** %f' %  (date, time.time())

print('\033[31;40;1m__name__  is %s\n\033[0m' % __name__)
pid = os.fork()
print(type(pid), pid, time.time(), sep= ' --- ')
print(invoke(),end = '\n\n')
##第一个等级顺序: 先执行父pid,     再执行子pid ;
# 第二个等级顺序: 然后先执行父代码,后执行子代码
#time.time()结果:
#  子代码 >  父代码  >   子pid >  父pid
#程序运行先后顺序1 :父pid;  2 :子pid;  3 :父代码; 4 :子代码

if pid:
  print('--- from  parent -----\n')
else:
  print('--- from  child  and  pid  is  %d -----\n' % pid )


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])

#[root@V0 devops_day01]# python3   forkzombie2.py 
#__name__  is __main__
#
#<class 'int'> --- 3288 --- 1555557331.6988096
#2019年*04月*18日 11时:15分:31秒
#-------**** 1555557331.698954
#
#--- from  parent -----
#
# sys.argv[0]  is forkzombie2.py
#
#<class 'int'> --- 0 --- 1555557331.6989071
#2019年*04月*18日 11时:15分:31秒
#-------**** 1555557331.699125
#
#--- from  child  and  pid  is  0 -----
#
# sys.argv[0]  is forkzombie2.py



#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
"""

import  sys, os, time

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

def  invoke():
  date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())
  return   '%s ----**** %f' %  (date, time.time())

pid = os.fork()

if pid:
  print('第一个等级顺序: 先执行父pid is %d ------ %s\n' % (pid, invoke()))

#•  父进程通过os.wait()来得到子进程是否终止的信息
#•  在子进程终止和父进程调用wait()之间的这段时间,
#子进程被称为zombie(僵尸)进程
#•  如果子进程还没有终止,  父进程先退出了,
#那么子进程会持续工作。
#系统自动将子进程的父进程设置为init进程,
#init将来负责清理僵尸进程

#•  waitpid()接受两个参数,
#第一个参数设置为 -1, 表示与wait()函数相同;
#第二参数 如果 设置为 0 表示 挂起 父进程,直到子程序退出,
#               设置为 1 表示 不挂起父进程
#>>> os.WNOHANG  #os模块的常量
#1
#•  waitpid()的返回值:
#如果子进程尚未结束则返回0,
#如果子进程 已经结束了, 就返回子进程的PID

  waitpid =  os.waitpid(-1, 0)
  print(type(waitpid), waitpid, sep = ' *** ', end = '---father\n')
  #<class 'tuple'> *** (2209, 0)---father

elif pid == 0:
  print('\n第一个等级顺序:    再执行子pid ;' )

  print(type(pid), pid, time.time(), sep= ' --- ', end = '--child子程序\n')
  for i in range(2):
    print(invoke())
    time.sleep(2)
  print('--- from  child  pid  is  %d , exit 退出子进程-----\n' % pid )

  #sys.exit()  直接退出程序，方法中包含一个参数status，
  #默认为0，表示正常退出， 
  #也可以为1， sys.exit(1)表示异常退出
  sys.exit()    #正常关闭退出子进程


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])

#[root@V0 devops_day01]# python3  sysexitos.py
#__name__ is __main__
#第一个等级顺序: 先执行父pid is 2209 ------ 2019年*04月*20日 10时:28分:40秒 ----**** 1555727320.143172
#
#
#第一个等级顺序:    再执行子pid ;
#<class 'int'> --- 0 --- 1555727320.1434586--child子程序
#2019年*04月*20日 10时:28分:40秒 ----**** 1555727320.143684
#2019年*04月*20日 10时:28分:42秒 ----**** 1555727322.146070
#--- from  child  pid  is  0 , exit 退出子进程-----
#
#<class 'tuple'> *** (2209, 0)---father
# sys.argv[0]  is sysexitos.py





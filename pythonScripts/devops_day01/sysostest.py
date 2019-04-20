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
elif pid == 0:
  print('\n第一个等级顺序:    再执行子pid ;' )
  print(type(pid), pid, time.time(), sep= ' --- ', end = '--child子程序\n')
  time.sleep(2)
  print(invoke())
  print('--- from  child  pid  is  %d , exit 退出子进程-----\n' % pid )
  #sys.exit()  直接退出程序，方法中包含一个参数status，
  #默认为0，表示正常退出， 
  #也可以为1， sys.exit(1)表示异常退出
  sys.exit()    #正常关闭退出子进程


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])

#[root@V0 devops_day01]# python3   sysostest.py
#__name__ is __main__
#第一个等级顺序: 先执行父pid is 2452 ------ 2019年*04月*20日 10时:50分:03秒 ----**** 1555728603.244712
#
# sys.argv[0]  is sysostest.py
#
#
#第一个等级顺序:    再执行子pid ;
#<class 'int'> --- 0 --- 1555728603.2449427--child子程序
#[root@V0 devops_day01]# 2019年*04月*20日 10时:50分:05秒 ----**** 1555728605.247578
#--- from  child  pid  is  0 , exit 退出子进程-----
#
#
#[root@V0 devops_day01]# 


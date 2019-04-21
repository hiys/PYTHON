#!/usr/bin/env  python3
#coding:UTF-8
import  sys, os, time, threading

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

num_a = 100

def  add(thr_name = ''):
  num_a = 0
  if thr_name :
    print('\n开始启动线程 %s -----在函数add()里面\n' % thr_name)
  for  i  in  range(40001000):
    num_a += 1
  print('\n在函数add() 里面改变局部变量num_a = %d --add' % num_a)
  return  num_a


def  add2(thr_name = ''):
  global   num_a
  if thr_name :
    print('\n开始启动线程 %s -------*add2()\n' % thr_name)
  time.sleep(1)
  print( '\n在函数add2()里面刚开始全局变量num_a的值 为 %d --*add2()' %  num_a)
  num_a += 200
  print('\n在函数add2() 里面改变全局变量num_a 的值为 %d --*add2()' % num_a)


def  sub():
  global   num_a
  time.sleep(1)
  print( '\n在函数sub()里面刚开始全局变量num_a的值 为 %d --sub()' %  num_a)
  num_a -=  30
  print('\n在函数sub() 里面改变全局变量num_a 的值为 %d --sub()' % num_a)


start = time.time()
for  i  in  range(3):  #单个进程, 3个人排队先后接力工作
  print(add())


print('一共运行的时间是 %f  --father'  %  (time.time()-start))



if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])


#[root@V0 devops_day01]# python3   timetest.py
#__name__ is __main__
#
#在函数add() 里面改变局部变量num_a = 40001000 --add
#40001000
#
#在函数add() 里面改变局部变量num_a = 40001000 --add
#40001000
#
#在函数add() 里面改变局部变量num_a = 40001000 --add
#40001000
#一共运行的时间是 4.178601  --father
# sys.argv[0]  is timetest.py
#
#[root@V0 devops_day01]#




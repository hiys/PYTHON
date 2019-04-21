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
#------------------产生 3个线程, 3个人排队工作
t1 = threading.Thread(target = add, args = ('thr1',))
t2 = threading.Thread(target = add, args = ('thr2',))
t3 = threading.Thread(target = add, args = ('thr3',))

t1.start()
t2.start()
t3.start()

t1.join()  #主线程挂起等待,直到线程t1 运行结束,才能接着执行主线程代码
t2.join()  #主线程挂起等待,直到线程t2 运行结束,才能接着执行主线程代码
t3.join()  #主线程挂起等待,直到线程t3 运行结束,才能接着执行主线程代码

print('一共运行的时间是 %f  线程thr1= %s\nthr2= %s\nthr3= %s\n ----father' \
  %  ((time.time() - start), t1, t2, t3))



if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])

#[root@V0 devops_day01]# python3  osfork_threadingtime2.py
#__name__ is __main__
#
#开始启动线程 thr1 -----在函数add()里面
#
#
#开始启动线程 thr2 -----在函数add()里面
#
#
#开始启动线程 thr3 -----在函数add()里面
#
#
#在函数add() 里面改变局部变量num_a = 40001000 --add
#
#在函数add() 里面改变局部变量num_a = 40001000 --add
#
#在函数add() 里面改变局部变量num_a = 40001000 --add
#一共运行的时间是 4.446637  线程thr1= <Thread(Thread-1, stopped 140521263605504)>
#thr2= <Thread(Thread-2, stopped 140521255212800)>
#thr3= <Thread(Thread-3, stopped 140521246820096)>
# ----father
# sys.argv[0]  is osfork_threadingtime2.py
#
#[root@V0 devops_day01]# 





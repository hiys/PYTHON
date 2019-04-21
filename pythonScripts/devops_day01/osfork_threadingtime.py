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
for  i  in  range(3):  #循环3次,产生 3个子进程, 3个人同时工作,不排队
  pid = os.fork()
  if  pid:
    print('第一个等级顺序: 先执行父pid is %d ---i= %d\n' % (pid, i))
  elif pid == 0:
    print(add())
    sys.exit()    #正常关闭退出子进程

waitpid =  os.waitpid(-1, 0)  #0挂起父进程,一直等到到子进程退出才执行下面的语句
waitpid_2 =  os.waitpid(-1, 0)  #0挂起父进程,一直等到到子进程退出才执行下面的语句
waitpid_3 =  os.waitpid(-1, 0)  #0挂起父进程,一直等到到子进程退出才执行下面的语句

print('一共运行的时间是 %f ---父进程一直等到确认子进程waitpid= %s ---waitpid_2 = %s \
 ---waitpid_3 = %s 已经退出 --father'  %  ((time.time() - start), waitpid, waitpid_2, waitpid_3) )



if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])

#[root@V0 devops_day01]# python3     osfork_threadingtime.py 
#__name__ is __main__
#第一个等级顺序: 先执行父pid is 4791 ---i= 0
#
#第一个等级顺序: 先执行父pid is 4792 ---i= 1
#
#第一个等级顺序: 先执行父pid is 4793 ---i= 2
#
#
#在函数add() 里面改变局部变量num_a = 40001000 --add
#40001000
#
#在函数add() 里面改变局部变量num_a = 40001000 --add
#40001000
#
#在函数add() 里面改变局部变量num_a = 40001000 --add
#40001000
#一共运行的时间是 2.208677 ---父进程一直等到确认子进程waitpid= (4791, 0) ---waitpid_2 = (4792, 0)  ---waitpid_3 = (4793, 0) 已经退出 --father
# sys.argv[0]  is osfork_threadingtime.py
#
#[root@V0 devops_day01]#



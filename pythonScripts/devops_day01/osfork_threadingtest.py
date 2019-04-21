#!/usr/bin/env  python3
#coding:UTF-8
import  sys, os, time, threading

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

num_a = 100

def  add(thr_name = ''):
  global   num_a
  if thr_name :
    print('\n开始启动线程 %s -----在函数add()里面\n' % thr_name)
  time.sleep(1)
  print( '\n在函数add()里面刚开始全局变量num_a的值 为 %d --add' %  num_a)
  num_a += 1000
  print('\n在函数add() 里面改变全局变量num_a 的值为 %d --add' % num_a)


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


pid = os.fork()

if pid:
  print('第一个等级顺序: 先执行父pid is %d \n' % pid)

  print( '\n在父进程里面刚开始的num_a的值 为 %d --father' %  num_a)

  t1 = threading.Thread(target = add, args = ('thr1',))
  t2 = threading.Thread(target = add2, args = ('thr2',))
  print('线程thr1= %s ----线程thr2= %s 将要启动thr1 ---father\n' % (t1, t2) )

  t1.start()
  t2.start()

  print('线程thr1 = %s ---- 线程thr2 = %s thr2也已经启动---father\n' % (t1, t2) )
  print('父进程里面的线程thr1= %s\nthr2= %s\n运行后的结果是%d---father\n' % (t1, t2, num_a))

  waitpid =  os.waitpid(-1, 0)  #0挂起父进程,一直等到到子进程退出才执行下面的语句
  print(type(waitpid), waitpid, sep = ' *** ', end = '---father\n')
  #

  print('父进程一直等到子进程退出,确认子进程已经退出 ---father\n')

  print('\n父进程里面的线程thr1= %s\nthr2= %s\n所有的程序运行后的最终结果是%d---father\n' % (t1, t2, num_a))


elif pid == 0:
  print('\n第一个等级顺序:    再执行子pid ;' )
  print( '\n在子进程里面刚开始的num_a的值 为 %d --child子程序' %  num_a)
  sub()
  print( '\n在子进程里面使用函数sub()改变num_a的值为 %d  --child子程序\n' %  num_a)

  sys.exit()    #正常关闭退出子进程



if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])

#[root@V0 devops_day01]# python3  osfork_threadingtest.py
#__name__ is __main__
#第一个等级顺序: 先执行父pid is 2670 
#
#
#在父进程里面刚开始的num_a的值 为 100 --father
#
#第一个等级顺序:    再执行子pid ;
#
#在子进程里面刚开始的num_a的值 为 100 --child子程序
#线程thr1= <Thread(Thread-1, initial)> ----线程thr2= <Thread(Thread-2, initial)> 将要启动thr1 ---father
#
#
#开始启动线程 thr1 -----在函数add()里面
#
#
#开始启动线程 thr2 -------*add2()
#
#线程thr1 = <Thread(Thread-1, started 140711305262848)> ---- 线程thr2 = <Thread(Thread-2, started 140711296870144)> thr2也已经启动---father
#
#父进程里面的线程thr1= <Thread(Thread-1, started 140711305262848)>
#thr2= <Thread(Thread-2, started 140711296870144)>
#运行后的结果是100---father
#
#
#在函数sub()里面刚开始全局变量num_a的值 为 100 --sub()
#
#在函数sub() 里面改变全局变量num_a 的值为 70 --sub()
#
#在子进程里面使用函数sub()改变num_a的值为 70  --child子程序
#
#
#在函数add()里面刚开始全局变量num_a的值 为 100 --add
#
#在函数add() 里面改变全局变量num_a 的值为 1100 --add
#
#在函数add2()里面刚开始全局变量num_a的值 为 1100 --*add2()
#
#在函数add2() 里面改变全局变量num_a 的值为 1300 --*add2()
#<class 'tuple'> *** (2670, 0)---father
#父进程一直等到子进程退出,确认子进程已经退出 ---father
#
#
#父进程里面的线程thr1= <Thread(Thread-1, stopped 140711305262848)>
#thr2= <Thread(Thread-2, stopped 140711296870144)>
#所有的程序运行后的最终结果是1300---father
#
# sys.argv[0]  is osfork_threadingtest.py
#
#[root@V0 devops_day01]# python3  osfork_threadingtest.py
#__name__ is __main__
#第一个等级顺序: 先执行父pid is 2682 
#
#
#在父进程里面刚开始的num_a的值 为 100 --father
#
#第一个等级顺序:    再执行子pid ;
#
#在子进程里面刚开始的num_a的值 为 100 --child子程序
#线程thr1= <Thread(Thread-1, initial)> ----线程thr2= <Thread(Thread-2, initial)> 将要启动thr1 ---father
#
#
#开始启动线程 thr1 -----在函数add()里面
#
#
#开始启动线程 thr2 -------*add2()
#线程thr1 = <Thread(Thread-1, started 140246472435456)> ---- 线程thr2 = <Thread(Thread-2, started 140246464042752)> thr2也已经启动---father
#
#
#父进程里面的线程thr1= <Thread(Thread-1, started 140246472435456)>
#thr2= <Thread(Thread-2, started 140246464042752)>
#运行后的结果是100---father
#
#
#在函数sub()里面刚开始全局变量num_a的值 为 100 --sub()
#
#在函数sub() 里面改变全局变量num_a 的值为 70 --sub()
#
#在子进程里面使用函数sub()改变num_a的值为 70  --child子程序
#
#
#在函数add2()里面刚开始全局变量num_a的值 为 100 --*add2()
#
#在函数add2() 里面改变全局变量num_a 的值为 300 --*add2()
#
#在函数add()里面刚开始全局变量num_a的值 为 300 --add
#
#在函数add() 里面改变全局变量num_a 的值为 1300 --add
#<class 'tuple'> *** (2682, 0)---father
#父进程一直等到子进程退出,确认子进程已经退出 ---father
#
#
#父进程里面的线程thr1= <Thread(Thread-1, stopped 140246472435456)>
#thr2= <Thread(Thread-2, stopped 140246464042752)>
#所有的程序运行后的最终结果是1300---father
#
# sys.argv[0]  is osfork_threadingtest.py
#
#[root@V0 devops_day01]# 



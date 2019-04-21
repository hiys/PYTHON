#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
  #sys.exit()  直接退出程序，方法中包含一个参数status，
  #默认为0，表示正常退出， 
  #也可以为1， sys.exit(1)表示异常退出
subtract   美 [səbˈtrækt]  
  v.减;减去
"""
import  sys, os, time, threading
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

def  invoke():
  date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())
  return   '%s ----**** %f' %  (date, time.time())


num_a = 100

def  add():
  global   num_a
  time.sleep(1)
  print( '\n在函数add()里面刚开始全局变量num_a的值 为 %d --add' %  num_a)
  num_a += 1000
  print('\n在函数add() 里面改变全局变量num_a 的值为 %d --add' % num_a)


def  add2():
  global   num_a
  time.sleep(2)
  print( '\n在函数add2()里面刚开始全局变量num_a的值 为 %d --*add2()' %  num_a)
  num_a += 200
  print('\n在函数add2() 里面改变全局变量num_a 的值为 %d --*add2()' % num_a)


def  sub():
  global   num_a
  time.sleep(3)
  print( '\n在函数sub()里面刚开始全局变量num_a的值 为 %d --sub()' %  num_a)
  num_a -=  30
  print('\n在函数sub() 里面改变全局变量num_a 的值为 %d --sub()' % num_a)


pid = os.fork()

if pid:
  print('第一个等级顺序: 先执行父pid is %d \n' % pid)
  #第一个等级顺序: 先执行父pid is 7723

  print( '\n在父进程里面刚开始的num_a的值 为 %d --father' %  num_a)
  #在父进程里面刚开始的num_a的值 为 100 --father

  add()
  print('在父进程里面使用函数add()改变num_a的值 为 %d --father\n' %  num_a)
#在函数add()里面刚开始全局变量num_a的值 为 100 --add
#
#在函数add() 里面改变全局变量num_a 的值为 1100 --add
#在父进程里面使用函数add()改变num_a的值 为 1100 --father

  #os.waitpid(-1, os.WNOHANG)的第一个参数设置为 -1, 表示与wait()函数相同;
#  waitpid =  os.waitpid(-1, os.WNOHANG)   #WNOHANG即值为1 表示 不挂起父进程
  #<class 'tuple'> *** (0, 0)---father  子进程尚未结束则返回0

  waitpid =  os.waitpid(-1, 0)  #0挂起父进程,一直等到到子进程退出才执行下面的语句
  print(type(waitpid), waitpid, sep = ' *** ', end = '---father\n')
  #<class 'tuple'> *** (7723, 0)---father
  print('父进程一直等到子进程退出,确认子进程已经退出 ---father\n')
  #父进程一直等到子进程退出,确认子进程已经退出 ---father

  t1 = threading.Thread(target = add)
  t2 = threading.Thread(target = add2)
  print('线程t1= %s ---- 线程t2 = %s' % (t1, t2) )
  t1.start()
  print('线程t1= %s ---- 线程t2 = %s' % (t1, t2) )
  t2.start()
  print('父进程里面的线程t1=%s \n t2 = %s \n运行后的结果是 %d' % (t1, t2, num_a))

#在函数add()里面刚开始全局变量num_a的值 为 1100 --add
#
#在函数add() 里面改变全局变量num_a 的值为 2100 --add
#
#在函数add2()里面刚开始全局变量num_a的值 为 2100 --*add2()
#
#在函数add2() 里面改变全局变量num_a 的值为 2300 --*add2()
#线程t1= <Thread(Thread-1, initial)> ---- 线程t2 = <Thread(Thread-2, initial)>
#线程t1= <Thread(Thread-1, stopped 139983096821504)> ---- 线程t2 = <Thread(Thread-2, initial)>
#父进程里面的线程t1=<Thread(Thread-1, stopped 139983096821504)> 
# t2 = <Thread(Thread-2, stopped 139983096821504)> 
#运行后的结果是 2300


elif pid == 0:
  print('\n第一个等级顺序:    再执行子pid ;' )
  print( '在子进程里面刚开始的num_a的值 为 %d --child子程序' %  num_a)
  sub()
  print( '在子进程里面使用函数sub()改变num_a的值为 %d  --child子程序\n' %  num_a)

  sys.exit()    #正常关闭退出子进程


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])

#[root@V0 devops_day01]# python3  osfork_threadingstart.py
#__name__ is __main__
#第一个等级顺序: 先执行父pid is 7723 
#
#
#在父进程里面刚开始的num_a的值 为 100 --father
#
#第一个等级顺序:    再执行子pid ;
#在子进程里面刚开始的num_a的值 为 100 --child子程序
#
#在函数add()里面刚开始全局变量num_a的值 为 100 --add
#
#在函数add() 里面改变全局变量num_a 的值为 1100 --add
#在父进程里面使用函数add()改变num_a的值 为 1100 --father
#
#
#在函数sub()里面刚开始全局变量num_a的值 为 100 --sub()
#
#在函数sub() 里面改变全局变量num_a 的值为 70 --sub()
#在子进程里面使用函数sub()改变num_a的值为 70  --child子程序
#
#<class 'tuple'> *** (7723, 0)---father
#父进程一直等到子进程退出,确认子进程已经退出 ---father
#
#
#在函数add()里面刚开始全局变量num_a的值 为 1100 --add
#
#在函数add() 里面改变全局变量num_a 的值为 2100 --add
#
#在函数add2()里面刚开始全局变量num_a的值 为 2100 --*add2()
#
#在函数add2() 里面改变全局变量num_a 的值为 2300 --*add2()
#线程t1= <Thread(Thread-1, initial)> ---- 线程t2 = <Thread(Thread-2, initial)>
#线程t1= <Thread(Thread-1, stopped 139983096821504)> ---- 线程t2 = <Thread(Thread-2, initial)>
#父进程里面的线程t1=<Thread(Thread-1, stopped 139983096821504)> 
# t2 = <Thread(Thread-2, stopped 139983096821504)> 
#运行后的结果是 2300
# sys.argv[0]  is osfork_threadingstart.py
#
#[root@V0 devops_day01]# 
#



#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
  #sys.exit()  直接退出程序，方法中包含一个参数status，
  #默认为0，表示正常退出， 
  #也可以为1， sys.exit(1)表示异常退出
subtract   美 [səbˈtrækt]  
       v.减;减去
  #os.waitpid(-1, os.WNOHANG)的第一个参数设置为 -1, 表示与wait()函数相同;
#  waitpid =  os.waitpid(-1, os.WNOHANG)   #WNOHANG即值为1 表示 不挂起父进程
  #<class 'tuple'> *** (0, 0)---father  子进程尚未结束则返回0
"""
import  sys, os, time, threading
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

lock = threading.Lock()   ## 生成lock实例

num_a = 100

def  add(thr_name = ''):
  return_value = lock.acquire()    #访问共享资源时,先请求锁
  print('type(return_value) = %s , return_value = %s) ' % (type(return_value), return_value))
  global   num_a
  if thr_name :
    print('\n开始启动线程 %s -----在函数add()里面\n' % thr_name)

  time.sleep(1)
  print( '\n在函数add()里面刚开始全局变量num_a的值 为 %d --add' %  num_a)
  num_a += 1000
  print('\n在函数add() 里面改变全局变量num_a 的值为 %d --add' % num_a)

  lock.release()   #访问共享资源结束后,立即释放锁

def  add2(thr_name = ''):

  lock.acquire()    #访问共享资源时,先请求锁

  global   num_a
  if thr_name :
    print('\n开始启动线程 %s -------*add2()\n' % thr_name)

  time.sleep(1)
  print( '\n在函数add2()里面刚开始全局变量num_a的值 为 %d --*add2()' %  num_a)
  num_a += 200
  print('\n在函数add2() 里面改变全局变量num_a 的值为 %d --*add2()' % num_a)

  lock.release()    #访问共享资源结束后,立即释放锁

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
  t2 = threading.Thread(target = add2,args = ('thr2',))
  t1.start()
  t2.start()
  t1.join()  #主线程挂起等待,直到线程t1 运行结束,才能接着执行主线程代码
  t2.join()  #主线程挂起等待,直到线程t2 运行结束,才能接着执行主线程代码

  print('\n线程thr1= %s ----线程thr2 = %s thr2全部已经结束了---father\n' % (t1, t2) )


  waitpid =  os.waitpid(-1, 0)  #0挂起父进程,一直等到到子进程退出才执行下面的语句
  print(type(waitpid), waitpid, sep = ' *** ', end = '---father\n')

  print('父进程一直等到子进程退出,确认子进程已经退出 ---father\n')
  #父进程一直等到子进程退出,确认子进程已经退出 ---father

  print('\n父进程里面的线程thr1= %s\nthr2= %s\n所有的程序运行后的最终结果num_a = %d ---father\n' % (t1, t2, num_a))


elif pid == 0:
  print('\n第一个等级顺序:    再执行子pid  --child子程序' )
  print( '\n在子进程里面刚开始的num_a的值 为 %d --child子程序' %  num_a)
  sub()
  print( '\n在子进程里面使用函数sub()改变num_a的值为 %d  --child子程序\n' %  num_a)

  sys.exit()    #正常关闭退出子进程


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])

#
#[root@V0 devops_day01]# python3   osfork_threadingLock.py 
#__name__ is __main__
#第一个等级顺序: 先执行父pid is 4020 
#
#
#在父进程里面刚开始的num_a的值 为 100 --father
#
#第一个等级顺序:    再执行子pid  --child子程序
#
#在子进程里面刚开始的num_a的值 为 100 --child子程序
#type(return_value) = <class 'bool'> , return_value = True) 
#
#开始启动线程 thr1 -----在函数add()里面
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
#开始启动线程 thr2 -------*add2()
#
#
#在函数add2()里面刚开始全局变量num_a的值 为 1100 --*add2()
#
#在函数add2() 里面改变全局变量num_a 的值为 1300 --*add2()
#
#线程thr1= <Thread(Thread-1, stopped 140102987835136)> ----线程thr2 = <Thread(Thread-2, stopped 140102906935040)> thr2全部已经结束了---father
#
#<class 'tuple'> *** (4020, 0)---father
#父进程一直等到子进程退出,确认子进程已经退出 ---father
#
#
#父进程里面的线程thr1= <Thread(Thread-1, stopped 140102987835136)>
#thr2= <Thread(Thread-2, stopped 140102906935040)>
#所有的程序运行后的最终结果num_a = 1300 ---father
#
# sys.argv[0]  is osfork_threadingLock.py
#
#[root@V0 devops_day01]# 



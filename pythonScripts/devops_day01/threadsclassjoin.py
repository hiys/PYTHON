#!/usr/bin/env  python3
"""#coding=UTF-8
一个进程就是一个应用程序的一次执行
进程 是 cpu 资源分配 的最小单位，
一个进程 至少 包括 一个线程
一个进程 可以 包含 多个线程，
进程：内存独立，
进程之间不能直接互相访问，同一进程中的线程可以互相通信

•  线程有 开始, 顺序执行 和 结束 三部分
•  线程的运行 可能 被抢占 (中断),
   或暂时的 被挂起 (也叫睡眠),
  让其它的线程运行, 这叫做让步
线程 是 cpu 调度     的最小单位
线程共享同一进程的内存，
线程是共享了 进程的 执行环境资源的 更为 细小的 CPU时间段
线程的结束 不会影响 同个进程中的 其他线程的运行状态
线程是轻量级的进程，
它的创建和销毁所需要的时间比进程小很多，

所有操作系统中的执行功能 都是 创建线程 去完成的
"""
import	 sys, os, time, threading

print('\033[31;40;1m__name__  is %s\n\033[0m' % __name__)

class  ThreadFunc(object):     #定义可调用的类
  def  __init__(self, func_invoke, args):

    #func_invoke 可以调用此自定义类外面的函数invoke(threadx, nseconds)
    self.func_invoke =  func_invoke 
    print('self.func_invoke = %s' % func_invoke )
#self.func_invoke = <function invoke at 0x7f4f03d05ea0>
#self.func_invoke = <function invoke at 0x7f4f03d05ea0>
#self.func_invoke = <function invoke at 0x7f4f03d05ea0>
#self.func_invoke = <function invoke at 0x7f4f03d05ea0>


    self.args = args  #可以调用的外面函数invoke(threadx, nseconds)的所有参数
    print('type(self.args)= %s ---self.args= %s' % (type(self.args),str(self.args)))
#type(self.args)= <class 'tuple'> ---self.args= ('thread_sec8', 8)
#type(self.args)= <class 'tuple'> ---self.args= ('thread_sec2', 2)
#type(self.args)= <class 'tuple'> ---self.args= ('thread_sec16', 16)
#type(self.args)= <class 'tuple'> ---self.args= ('thread_sec4', 4)

  def  __call__(self): #调用call内建方法可在这个类的外面把此类型对象当作函数来使用
    #*表示args 是个元组,传参时，实参以元组的形式进行传递
    self.func_invoke(*self.args)


def  invoke(threadx, nseconds):   #定义函数,打印运行的起止时间
  "threadx是个字符串类型,说明一个线程的自定义名字"
  print('\n开始启动线程 %s 将要休眠 %d 秒\n' % (threadx, nseconds) )

  time.sleep(nseconds)   #设置休眠 nseconds 秒

  date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())

  print('线程%s 运行结束时间是 %s\n-------------------**** %f\n' \
   %  (threadx, date, time.time()))

def  main():
  print('%s 主程序开始的时间点是: %s'  % \
  (time.strftime('%Y年*%m月*%d日%H时:%M分:%S秒',time.localtime()), time.time()))
  #2019年*04月*19日14时:26分:34秒 主程序开始的时间点是: 1555655194.9640627

  threadnamelist = ['thread_sec8', 'thread_sec2', 'thread_sec16', 'thread_sec4']
  secondlist = [ 8, 2, 16, 4]  # 创建 休眠列表
  threadlist = []     #创建线程空列表

  for i in range(4):  #创建4 个线程,放入列表threadlist
    #传递可调用类ThreadFunc(object) 给Thread类
    thx = threading.Thread(target = ThreadFunc( func_invoke = invoke, args= (threadnamelist[i], secondlist[i]) ) )

    print(thx, type(thx), threadnamelist[i], sep= ' -*- ', end = '\n\n')
    #<Thread(Thread-1, initial)> -*- <class 'threading.Thread'> -*- thread_sec8
    #<Thread(Thread-2, initial)> -*- <class 'threading.Thread'> -*- thread_sec2
    #<Thread(Thread-3, initial)> -*- <class 'threading.Thread'> -*- thread_sec16
    #<Thread(Thread-4, initial)> -*- <class 'threading.Thread'> -*- thread_sec4


    threadlist.append(thx) #在列表threadlist中追加threading.Thread类对象实例thx
				
  for  i  in range(4):
    print('\n开始启动线程 %s ( %s ) 执行 ---' %  (threadlist[i], threadnamelist[i]))
    #开始启动线程 <Thread(Thread-1, initial)> ( thread_sec8 ) 执行 ---
    #开始启动线程 <Thread(Thread-2, initial)> ( thread_sec2 ) 执行 ---
    #开始启动线程 <Thread(Thread-3, initial)> ( thread_sec16 ) 执行 ---
    #开始启动线程 <Thread(Thread-4, initial)> ( thread_sec4 ) 执行 ---

    #Thread对象使用start()方法开始线程的执行
    threadlist[i].start() #启动线程执行
    #开始启动线程 thread_sec8 将要休眠 8 秒
    #开始启动线程 thread_sec2 将要休眠 2 秒
    #开始启动线程 thread_sec16 将要休眠 16 秒
    #开始启动线程 thread_sec4 将要休眠 4 秒

  for  i  in range(4):
    print('\n正在使用主线程%s ( %s ) 的join()方法' %  (threadlist[i], threadnamelist[i]))
    threadlist[i].join()  #主线程挂起,直到另外一个线程结束,才能接着执行主线程代码

    #正在使用主线程<Thread(Thread-1, started 139977214486272)> ( thread_sec8 ) 的join()方法
    #线程thread_sec2 运行结束时间是 2019年*04月*19日 14时:26分:36秒
    #-------------------**** 1555655196.967934
    #
    #线程thread_sec4 运行结束时间是 2019年*04月*19日 14时:26分:38秒
    #-------------------**** 1555655198.970218
    #
    #线程thread_sec8 运行结束时间是 2019年*04月*19日 14时:26分:42秒
    #-------------------**** 1555655202.972914
    #
    #
    #正在使用主线程<Thread(Thread-2, stopped 139977206093568)> ( thread_sec2 ) 的join()方法
    #
    #正在使用主线程<Thread(Thread-3, started 139977197700864)> ( thread_sec16 ) 的join()方法
    #线程thread_sec16 运行结束时间是 2019年*04月*19日 14时:26分:50秒
    #-------------------**** 1555655210.982123
    #
    #
    #正在使用主线程<Thread(Thread-4, stopped 139977189308160)> ( thread_sec4 ) 的join()方法
 

  print('\n所有的线程在 %s 运行结束,具体时间点是 %f' % (time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime()), time.time()))
  #所有的线程在 2019年*04月*19日 14时:26分:50秒 运行结束,具体时间点是 1555655210.982632

  print(invoke.__name__, type(invoke.__name__),sep = ' --*-- ')
  #invoke --*-- <class 'str'>
 

if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])
  main()




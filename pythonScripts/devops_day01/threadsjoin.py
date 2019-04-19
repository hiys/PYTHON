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
  #2019年*04月*19日11时:47分:01秒 主程序开始的时间点是: 1555645621.7719293

  threadnamelist = ['thread_sec8', 'thread_sec2', 'thread_sec16', 'thread_sec4']
  secondlist = [ 8, 2, 16, 4]  # 创建 休眠列表
  threadlist = []     #创建线程空列表

  for i in range(4):  #创建4 个线程,放入列表threadlist
  #传递函数给threading.Thread类
  #多线程编程方法之一 ------ 传递函数给threading模块的Thread类
  #第一个参数target指定目标函数名， 
  #第二个参数args是一个元组，是前面指定的函数名的参数元组,如果只传递一个参数值，必须在参数值后添加一个逗号",", 不能少，少了就不是元组了

    thx = threading.Thread(target = invoke, args= (threadnamelist[i], secondlist[i]))
    print(thx, type(thx), threadnamelist[i], sep= ' -*- ', end = '\n\n')
    #<Thread(Thread-1, initial)> -*- <class 'threading.Thread'> -*- thread_sec8
    #<Thread(Thread-2, initial)> -*- <class 'threading.Thread'> -*- thread_sec2
    #<Thread(Thread-3, initial)> -*- <class 'threading.Thread'> -*- thread_sec16
    #<Thread(Thread-4, initial)> -*- <class 'threading.Thread'> -*- thread_sec4

    threadlist.append(thx) #在列表threadlist中追加threading.Thread类对象实例thx
				
  for  i  in range(4):
    print('\n开始启动线程 %s ( %s ) 执行 ---' %  (threadlist[i], threadnamelist[i]))

    #Thread对象使用start()方法开始线程的执行
    threadlist[i].start() #启动线程执行

    #开始启动线程 <Thread(Thread-1, initial)> ( thread_sec8 ) 执行 ---
    #开始启动线程 thread_sec8 将要休眠 8 秒
    #
    #开始启动线程 <Thread(Thread-2, initial)> ( thread_sec2 ) 执行 ---
    #开始启动线程 thread_sec2 将要休眠 2 秒
    #
    #开始启动线程 <Thread(Thread-3, initial)> ( thread_sec16 ) 执行 ---
    #开始启动线程 thread_sec16 将要休眠 16 秒
    #
    #开始启动线程 <Thread(Thread-4, initial)> ( thread_sec4 ) 执行 ---
    #开始启动线程 thread_sec4 将要休眠 4 秒


  for  i  in range(4):
  #join()方法: Thread对象threadlist[i]这个主线程在执行过程中要调用另外一个线程，
  #并且等到另外一个线程 完成 以后 才能接着执行主线程的代码
  #join([time]): 等待至线程中止。
  #这阻塞调用线程直至线程的join() 方法被调用中止-正常退出
  #或者抛出未处理的异常-或者是可选的超时发生。
    print('\n正在使用主线程%s ( %s ) 的join()方法' %  (threadlist[i], threadnamelist[i]))
    #主线程挨个调用子线程的threadlist[i].join()方法。
    #当所调用的线程threadlist[i] 都执行完毕后，主线程才会执行主线程代码
    threadlist[i].join()  #主线程挂起,直到另外一个线程结束,才能接着执行主线程代码

    #正在使用主线程<Thread(Thread-1, started 139738681808640)> ( thread_sec8 ) 的join()方法
    #线程thread_sec2 运行结束时间是 2019年*04月*19日 11时:47分:03秒
    #-------------------**** 1555645623.774828
    #
    #线程thread_sec4 运行结束时间是 2019年*04月*19日 11时:47分:05秒
    #-------------------**** 1555645625.776901
    #
    #线程thread_sec8 运行结束时间是 2019年*04月*19日 11时:47分:09秒
    #-------------------**** 1555645629.780668
    #
    #
    #正在使用主线程<Thread(Thread-2, stopped 139738673415936)> ( thread_sec2 ) 的join()方法
    #
    #正在使用主线程<Thread(Thread-3, started 139738665023232)> ( thread_sec16 ) 的join()方法
    #线程thread_sec16 运行结束时间是 2019年*04月*19日 11时:47分:17秒
    #-------------------**** 1555645637.788953
    #
    #
    #正在使用主线程<Thread(Thread-4, stopped 139738656630528)> ( thread_sec4 ) 的join()方法

  print('\n所有的线程在 %s 运行结束,具体时间点是 %f' % (time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime()), time.time()))
  #所有的线程在 2019年*04月*19日 11时:47分:17秒 运行结束,具体时间点是 1555645637.789410


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])
  main()




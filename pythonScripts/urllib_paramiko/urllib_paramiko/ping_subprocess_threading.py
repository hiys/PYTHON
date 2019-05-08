#!/usr/bin/env  python3
"""#coding=UTF-8
[root@V0 devops_day01]# type  lscpu 
lscpu 是 /usr/bin/lscpu
[root@V0 devops_day01]# rpm   -qf  /usr/bin/lscpu
util-linux-2.23.2-43.el7.x86_64

[root@V0 devops_day01]# lscpu |grep  -i cpu
CPU op-mode(s):        32-bit, 64-bit
CPU(s):                2
On-line CPU(s) list:   0,1
CPU 系列：          6
CPU MHz：             3191.994
NUMA 节点0 CPU：    0,1
  Central  Progressing  Unit 中央处理器，
是一块超大规模的集成电路，是一台计算机的运算核心和控制核心
CPU包括 运算器，高速缓冲存储器，总线

操作系统调度器：拆分CPU为一段段时间的运行片，轮流分配给不同的程序
进程 是 cpu 资源分配 的最小单位
线程 是 cpu 调度     的最小单位

CPU调度的是线程, 系统为进程分配资源，不对线程分配资源
多个CPU多个任务: 
在同一时间点运行多个线程, 哪个线程在哪个CPU执行，跟操作系统和CPU本身的设计有关
多线程，实际上是计算机多种资源(cpu,网络, 内存,硬盘,显示器等)的并行运用，
与CPU的数量没关系
"""
import	 sys, time, threading, subprocess

print('\033[31;40;1m__name__  is %s\n\033[0m' % __name__)

def  invoke():
  date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())
  return   '%s --** %f' %  (date, time.time())



def  ping(thr_name,host): #定义函数,打印运行的结束时间

  print('\n开始启动线程 %s ,ping测试主机ip是 %s' % (thr_name, host))

  hostping = 'ping  -c2  -w0.4  -i0.2  %s &> /dev/null' %  host
  rc = subprocess.call( hostping , shell = True)

  if rc == 0 :
    varstr = 'host %s: is up' % host
  else:
    varstr = 'host %s: is down' % host
  print('线程%s 运行结束时间是%s ping结果%s\n' %  (thr_name,  invoke(), varstr))



if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])
  hosts = ['192.168.0.%d' % ip for  ip in  range(9, 14)]
  print(hosts)
  #['192.168.0.9', '192.168.0.10', '192.168.0.11', '192.168.0.12', '192.168.0.13']
  start = time.time()
  threadlist = []     #创建线程空列表

  #创建函数ping(thr_name,host) 的参数thr_name 列表
  thr_namelist = ['thr_1','thr_2','thr_3','thr_4','thr_5']
  
  for  i   in   range(len(hosts)): #创建5 个线程,放入列表threadlist
    thr = threading.Thread(target = ping, args = (thr_namelist[i], hosts[i]) )
    print(thr, type(thr), thr_namelist[i], sep= ' -*- ', end = '\n\n')
#<Thread(Thread-1, initial)> -*- <class 'threading.Thread'> -*- thr_1
#<Thread(Thread-2, initial)> -*- <class 'threading.Thread'> -*- thr_2
#<Thread(Thread-3, initial)> -*- <class 'threading.Thread'> -*- thr_3
#<Thread(Thread-4, initial)> -*- <class 'threading.Thread'> -*- thr_4
#<Thread(Thread-5, initial)> -*- <class 'threading.Thread'> -*- thr_5

    #在列表threadlist中追加threading.Thread类对象实例thr
    threadlist.append(thr)

  for  i  in  range(len(hosts)):
    print('\n开始启动线程%s ( %s )执行---' %  (threadlist[i], thr_namelist[i]))

    threadlist[i].start() #启动线程执行
#开始启动线程<Thread(Thread-1, initial)> ( thr_1 )执行---
#开始启动线程 thr_1 ,ping测试主机ip是 192.168.0.9
#
#开始启动线程<Thread(Thread-2, initial)> ( thr_2 )执行---
#开始启动线程 thr_2 ,ping测试主机ip是 192.168.0.10
#
#开始启动线程<Thread(Thread-3, initial)> ( thr_3 )执行---
#开始启动线程 thr_3 ,ping测试主机ip是 192.168.0.11
#
#开始启动线程<Thread(Thread-4, initial)> ( thr_4 )执行---
#开始启动线程 thr_4 ,ping测试主机ip是 192.168.0.12
#
#开始启动线程<Thread(Thread-5, initial)> ( thr_5 )执行---
#开始启动线程 thr_5 ,ping测试主机ip是 192.168.0.13


  for  i  in  range(len(hosts)):
    print('\n正在使用主线程%s ( %s ) 的join()方法' % (threadlist[i], thr_namelist[i]) )
    threadlist[i].join()

#正在使用主线程<Thread(Thread-1, started 140577080219392)> ( thr_1 ) 的join()方法
#线程thr_2 运行结束时间是2019年*04月*20日 16时:09分:05秒 --** 1555747745.327674 ping结果host 192.168.0.10: is up
#
#线程thr_4 运行结束时间是2019年*04月*20日 16时:09分:05秒 --** 1555747745.328277 ping结果host 192.168.0.12: is up
#
#线程thr_3 运行结束时间是2019年*04月*20日 16时:09分:05秒 --** 1555747745.328671 ping结果host 192.168.0.11: is up
#
#线程thr_1 运行结束时间是2019年*04月*20日 16时:09分:08秒 --** 1555747748.131729 ping结果host 192.168.0.9: is down
#
#
#正在使用主线程<Thread(Thread-2, stopped 140577071826688)> ( thr_2 ) 的join()方法
#
#正在使用主线程<Thread(Thread-3, stopped 140577063433984)> ( thr_3 ) 的join()方法
#
#正在使用主线程<Thread(Thread-4, stopped 140577055041280)> ( thr_4 ) 的join()方法
#
#正在使用主线程<Thread(Thread-5, started 140577046648576)> ( thr_5 ) 的join()方法
#线程thr_5 运行结束时间是2019年*04月*20日 16时:09分:08秒 --** 1555747748.135612 ping结果host 192.168.0.13: is down


  print('\n所有的线程在 %s 运行结束,一共花费的时间是 %f' % (invoke(), (time.time() - start)))
  #一共花费的时间是 0.000671 #os.fork()多进程的结果
#加了threadlist[i].join() 的结果
#所有的线程在 2019年*04月*20日 16时:09分:08秒 --** 1555747748.135941 运行结束,一共花费的时间是 3.015897

#没有threadlist[i].join(),仅仅只有threadlist[i].start()的结果
#  for  i  in  range(len(hosts)):
#    print('\n正在使用主线程%s ( %s ) 的join()方法' % (threadlist[i], thr_namelist[i]) )
#    threadlist[i].join()

#所有的线程在 2019年*04月*20日 16时:20分:04秒 --** 1555748404.981257 运行结束,一共花费的时间是 0.009313


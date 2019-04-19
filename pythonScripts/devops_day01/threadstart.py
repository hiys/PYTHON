#!/usr/bin/env  python3
"""#coding=UTF-8
"""
import	 sys, os, time, threading

def  invoke():
  date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())
  return   '%s\n-------**** %f' %  (date, time.time())

print('\033[31;40;1m__name__  is %s\n\033[0m' % __name__)

nums = [4, 2]

def  loop(nloop, nsecond):  #定义函数,打印运行的起止时间
  print('start  loop %d, at %s' % (nloop,time.ctime()))
#start  loop 0, at Thu Apr 18 20:37:02 2019
#start  loop 0, at Thu Apr 18 20:37:02 2019

  time.sleep(nsecond)

  print('loop %d done  at %s' % (nloop,time.ctime()))
#loop 0 done  at Thu Apr 18 20:37:04 2019
#loop 0 done  at Thu Apr 18 20:37:06 2019

def  main():
  print('starting at: %s' % time.ctime())
  #创建线程列表
  threads = []
  for i in range(2): #创建两个线程,放入列表
    #传递函数给threading.thread类
   #多线程编程方法之一 ------ 传递函数给threading模块的thread类

    #target 指定目标函数, args 是函数loop(nloop, nsecond)需要传入的参数
    t = threading.Thread(target = loop, args= (0, nums[i]))
    print(t, type(t),sep= ' -*- ', end = '\n\n')
#<Thread(Thread-1, initial)> -*- <class 'threading.Thread'>
#<Thread(Thread-2, initial)> -*- <class 'threading.Thread'>

    threads.append(t) #在列表threads中追加threading.Thread类对象实例t
				
  for  i  in range(2):
  #thread对象使用start()方法开始线程的执行
    threads[i].start() #同时运行两个线程
  for  i  in range(2):
  #thread对象使用join()方法挂起程序,直到线程结束
    threads[i].join()  #主程序挂起,直到所有线程结束
  print('all Done at %s' % time.ctime())
#all Done at Thu Apr 18 20:37:06 2019


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])
  main()




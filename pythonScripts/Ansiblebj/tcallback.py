#!/usr/bin/env  python
# -*- coding: utf8 -*-
'''
定义源文件的编码方式，使用流行编辑器中的格式化方式
# -*- coding:utf8 -*-
# -*- coding:latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding:ascii -*-
#coding:UTF-8
#coding=UTF-8
interpreter         美 [ɪnˈtɜːrprətər]  
      n.口译工作者;口译译员;演绎(音乐、戏剧中人物等)的人;解释程序

[root@V3 ansible]# pip3  install  pyflakes
Looking in indexes: http://pypi.doubanio.com/simple/
Collecting pyflakes
  Downloading http://pypi.doubanio.com/packages/84/f2/ed0ffb887f8138a8fe5a621b8c0bb9598bfb3989e029f6c6a85ee66628ee/pyflakes-2.1.1-py2.py3-none-any.whl (59kB)
     |████████████████████████████████| 61kB 3.4MB/s 
Installing collected packages: pyflakes
Successfully installed pyflakes-2.1.1
[root@V3 ansible]# pyflakes   tcallback.py
[root@V3 ansible]# echo  $?
0
'''
import   called, sys
#__name__ is called

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)
#__name__ is __main_

#软件模块之间存在接口，调用方式分为三类：同步调用、回调和异步调用
#回调是一种双向调用模式，被调用方在接口被调用时也会调用对方的接口
#回调常常是异步调用的基础

#函数call_fun(play_fun)有相应的内存空间，这里的play_fun代表一个函数，
#函数play_fun也有相应的地址，
#将函数callback_a的指针(内存地址)作为参数play_fun传递给另外一个函数call_fun(play_fun)使用，
#另外的这个函数call_fun(play_fun)调用了指针(callback_a的内存地址)所指向地址的内容callback_a()
#用函数指针(callback_a的内存地址)充当函数名play_fun，去调用函数体callback_a()。
#callback_a()就是回调函数


#回调函数简称回调(callback),调用者甲方tcallback.py也称之为应用方程序
#调用者甲方tcallback.py的回调函数callback_a,回调函数callback_b,回调函数callback_c,
#被调用者乙方called.py的功能函数call_fun
def callback_a():
  print('------ Aa ------tcallback.py')
  called.time.sleep(4)
  print("in callback_a ------ tcallback.py")
  return  'Aa -- tcallback.py'

def callback_b():
  print('--- Bb ----- tcallback.py')
  called.time.sleep(2)
  print("in callback_b ------ tcallback.py")
  return  'Bb -- tcallback.py'

def callback_c():
  print('------ Cc -------- tcallback.py')
  called.time.sleep(4)
  print("in callback_c ------ tcallback.py")
  return  'Cc -- tcallback.py'


def   main():
  print('callback_a = %s\n' % callback_a)
  #callback_a = <function callback_a at 0x7f52a59e46e0>

  play_fun = callback_a  # 使用我们的自定义参数callback_a函数
  print('play_fun =  %s\n' %  play_fun)
  #play_fun =  <function callback_a at 0x7f52a59e46e0>

  result = called.call_fun(play_fun) #执行回调函数
  print('\nresult = %s\n' % result)
  #------- in call_fun **** called.py -------
  #
  #------ Aa ------tcallback.py
  #in callback_a ------ tcallback.py
  #
  #result = **Aa -- tcallback.py * called.py**

  print('***' * 5)
  #***************

  play_fun = callback_b      # 使用我们的自定义参数callback_a函数
##被调用者乙方called.py的功能函数call_fun,也称之为库函数call_fun
  #注意called.call_fun是功能函数, callback_b是回调函数
  result = called.call_fun(play_fun)     #执行回调函数callback_b()
  print('\nresult = %s\n' % result)
  print('END---OVER')
  #------- in call_fun **** called.py -------
  #
  #--- Bb ----- tcallback.py
  #in callback_b ------ tcallback.py
  #
  #result = **Bb -- tcallback.py * called.py**
  #
  #END---OVER


if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)
  #sys.argv is ['tcallback.py']
  main()






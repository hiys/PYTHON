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
....................
[root@V3 ansible]# pyflakes   called.py
[root@V3 ansible]# echo  $?
0
'''
import   time, sys
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

#被调用者乙方called.py的功能函数call_fun,也称之为库函数call_fun
#这个被传入的play_fun参数后来又被调用的play_fun()函数称之为回调函数
def  call_fun(play_fun):
  print("\n------- in call_fun **** called.py -------\n")
#被调用者乙方called.py 调用甲方tcallback.py的回调函数(例如callback_a)的操作动作，称其为回调操作
  varx = play_fun() + " * called.py"
  time.sleep(8)
  return  '**%s**' % varx


if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)
  print("\n-------- ****** called.py  ****** -------\n")

#[root@V3 ansible]# python     called.py
#__name__ is __main__
#sys.argv is ['called.py']
#
#-------- ****** called.py  ****** -------
#
#[root@V3 ansible]# 



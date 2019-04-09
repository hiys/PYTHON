#!/usr/bin/env  python3
import  sys, os, pickle, time, random
#from  functools  import  reduce
#from  functools  import  partial
#import  tkinter    # tk-devel  tcl-devel 是模版tkinter依赖的软件包
#import  sqlite3    # sqlite-devel sqlite #模版sqlite3 依赖的软件包 

"MoBan ------------ instruction"
print('\033[31;47;1m__name__  is %s\033[0m' %  __name__)

date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())

def  loop():
  endlist = []
  for i in range(1,5):
    endlist.append(i)
    time.sleep(0.1)
  print(date)
  return  endlist     #返回的是一个列表数据


def  timetest(functionx):
  start = time.time()
  result = functionx()  #result获取的是一个列表数据(如果参数functionx = loop的话)
  return  time.time() - start, result    #返回元组数据类型


# decorate    装饰;布置
def  decorate(func):

  def  timetit():   #内部函数timeit() 和 timetest(functionx) 的作用是一样的
    start = time.time()
    result = func()   #result获取的是一个列表数据(如果参数func = loop的话)
    return time.time() -start, result    #返回元组数据类型
  return  timetit


@decorate      #@decorate 装饰器 的作用等同于loop_2 = decorate(loop_2)
def  loop_2():
  endlist = []
  for i in range(1,5):
    endlist.append(i)
    time.sleep(0.1)
  print(date)
  return  endlist     #返回的是一个列表数据




if __name__ == '__main__':
  print('\033[30;43;1m sys.argv  is %s\033[0m\n' % sys.argv)

  received = timetest(loop)
  #2019年*04月*09日 19时:25分:58秒  
  print(type(received),received,sep= ' ---',end = ' --timetest(loop)\n\n')
  #<class 'tuple'> ---(0.4012415409088135, [1, 2, 3, 4]) --timetest(loop)  


  received_2 = loop()
  #2019年*04月*09日 19时:25分:58秒
  print(type(received_2),received_2,sep= ' $$  ',end = ' --loop()\n\n')
  #<class 'list'> $$  [1, 2, 3, 4] --loop()


  loop = decorate(loop)  #返回的是一个内部函数timeit()
                #调用函数timeit() 会 返回一个元组类型的数据
  # 效果等于直接使用函数timetest(loop),会 返回一个元组类型的数据
  received_3 = loop()
  #2019年*04月*09日 19时:25分:58秒
  print(type(received_3),received_3,sep= '  ***  ',end = ' --decorate(loop)\n\n')
  #<class 'tuple'>  ***  (0.4016764163970947, [1, 2, 3, 4]) --decorate(loop)

   
  #不修改原有的旧函数,但是改变了函数的功能,别人可以把此函数按照习惯用法来使用
  received_4 = loop_2()   #不修改原有的旧函数
  #2019年*04月*09日 19时:25分:58秒
  print(type(received_4),received_4,sep= ' ###  ',end = ' --loop_2()\n')
  #<class 'tuple'> ###  (0.40166783332824707, [1, 2, 3, 4]) --loop_2()





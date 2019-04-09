#!/usr/bin/env  python3
import  sys, os, time

"MoBan ------------ instruction"
print('\033[31;47;1m__name__  is %s\033[0m' %  __name__)

date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())

# decorate  装饰器

def  new_function(formal_old):
  def  inside():   #内部函数inside() 和 inside(formal_old) 的作用是一样的
    result = formal_old()  #result = 一个日期字符串数据(若参数formal_old = old_function)
    return  result + ' inside_string'  #返回" 日期+ ' inside_string'" 字符串数据类型
  return  inside


@new_function   #@new_function 装饰器的作用等同于old_function = new_function(old_function)
def  old_function():
  return   date      #返回的是一个日期

@new_function
def  old_func2():
  return '\033[32;46;1m old_func2 \t\033[0m'


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv  is %s\033[0m\n' % sys.argv)
   
  #不修改原有的旧函数,但是改变了函数的功能,别人可以把此函数按照习惯用法来使用
  received = old_function()   #不修改原有的旧函数
  
  print(type(received),received,sep= ' ###  ',end = ' --new_function(old_function)()\n')
  #<class 'str'> ###  2019年*04月*09日 20时:55分:17秒 inside_string --new_function(old_function)()
  

  print(old_func2())
  # old_func2 	 inside_string



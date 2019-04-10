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



#生成器
#•  从句法上讲,生成器是一个带yield语句的函数
#•  一个函数或者子程序只返回一次,
#但一个生成器能暂停执行
#并返回一个中间的结果
#•  yield 语句返回一个值给调用者并暂停执行
#•  当生成器的next()方法被调用的时候,
#它会准确地从离开地方继续
def  simple_generator():
  yield  100
  yield  'hello world'
  yield  [ 1, 2, 3]



def  outfile():  
  def  fileblock(fobj):
    block = []
    lines = 0
    for  line  in  fobj:
      block.append(line)
      lines += 1
      if lines == 3:
        yield  block
        lines = 0
        block = []
        print('---for line in  fobj ---\n')
    if block:  #若有3的整数倍的行剩余,yield 语句返回一个值给调用者
      yield  block
  
  #[root@V0 day06]# wc  -l  /root/pyscripts/day06/mima 
  #8 /root/pyscripts/day06/mima
  
  fname = '/root/pyscripts/day06/mima'
  
  fobj = open(fname)
  blocks = fileblock(fobj)
  for block  in blocks:
    print(block)
  fobj.close()
  
  print( '\n--------- with as 方式 ---------\n')
  
  with open(fname)  as  fobj:
    for block in  fileblock(fobj):
      print(block)





if __name__ == '__main__':
  print('\033[30;43;1m sys.argv  is %s\033[0m\n' % sys.argv)
   
  #不修改原有的旧函数,但是改变了函数的功能,别人可以把此函数按照习惯用法来使用
  received = old_function()   #不修改原有的旧函数
  
  print(type(received),received,sep= ' ###  ',end = ' --new_function(old_function)()\n')
  #<class 'str'> ###  2019年*04月*09日 20时:55分:17秒 inside_string --new_function(old_function)()
  

  print(old_func2())
  # old_func2 	 inside_string

  a = simple_generator()
  print(type(a),a, sep= ' ---type(a) -- a --')
  #<class 'generator'> ---type(a) -- a --<generator object simple_generator at 0x7f5004df4200>

  print(a.__next__())   #python 3.4.3要使用c.__next__()不能使用c.next()
  # 100
  print(a.__next__())   #python 3.4.3要使用c.__next__()不能使用c.next()
  #hello world

  print('-----------------') 
  #-----------------
  print(a.__next__()) 
  #[1, 2, 3]

#当到达一个真正的返回或者函数结束没有更多的值返回,
#StopIteration异常就会被抛出
#  print(a.__next__())   
  #Traceback (most recent call last):
  # File "simple_generator.py", line 61, in <module>
  #    print(a.__next__())   
  #StopIteration


  outfile()






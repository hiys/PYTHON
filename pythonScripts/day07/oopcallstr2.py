#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8 专门为版本2 解决默认编码问题,可以识别中文"""

import  sys
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

class  Book:
  def  __init__(self, title, author):
    "author [ˈɔ:θə(r)] n. 作者;著作家;创造者;发起人"
    self.title = title
    self.author = author

  def  __str__(self):   #打印/显示实例时调用内建方法str
    return '<Book: %s>' % self.title


  def  __call__(self): #调用call内建方法可把此类型对象当作函数来使用
    print('<< %s >> is written by %s !' % (self.title, self.author))


class   Number:
  def __init__(self, num):
    self.num = num

  #__add__方法并不支持＋运算符右侧使用实例对象
  def __add__(self, other):  # add 默认实例的对象位置在运算符"+"的左边
    return   self.num + other

 #＋右侧的对象是类实例，左边对象不是类实例，调用__radd__内建方法
  def __radd__(self, other): # radd 默认实例的对象位置在运算符"+"的右边
    return   self.num + other + 9


  def __sub__(self, other):
    return  self.num - other

  def __rsub__(self, other):  #在运算符 - 右侧的对象是类实例
    return  self.num - other - 10
  

  def __mul__(self, other):
    return  self.num * other 
  def __rmul__(self, other):  #在运算符 * 右侧的对象是类实例
    return  self.num * other * 10

  def __truediv__(self, other):
    return  self.num / other
  def __rtruediv__(self, other):   #在运算符 / 右侧的对象是类实例
    return  self.num / other


  #
  def  __gt__(self, other):  #gt大于号比较
    return  self.num > other

  def __ge__(self, other):
    return  self.num >= other

  def  __eq__(self, other):
    return self.num == other

  def __le__(self, other):
    return self.num <= other

  def __lt__(self, other):
    return  self.num < other

  def __ne__(self, other):
    return  self.num  !=  other



if  __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)
  pybook = Book('Core Python', 'Wesley Chun')
  print(pybook,type(pybook),sep = ' ---- ')  #自动调用方法__str__

#<__main__.Book object at 0x7f5df0f202b0> ---- <class '__main__.Book'>
#替换成了下一行
  #<Book: Core Python> ---- <class '__main__.Book'>

  pybook()   #自动调用方法 __call__
  #<< Core Python >> is written by Wesley Chun !

  nx1 = Number(10)
  print(nx1 + 100) # add 默认实例的对象位置在运算符"+"的左边(nx1+ 100)
  #110
  print(100 + nx1) # radd 默认实例的对象(如nx1)位置在运算符"+" 的右边
  #119

  print('nx1 - 5 = ', nx1 - 5)
  #nx1 - 5 =  5

  print('nx1 - 5 = ', 5 - nx1)
  #nx1 - 5 =  -5  #return  self.num - other - 10

  print('nx1 * 5 = ', nx1 * 5)
  #nx1 * 5 =  50
  print('nx1 * 5 = ', 5 * nx1)
  # nx1 * 5 =  500             #return  self.num * other * 10
  #原因__rmul__(self, other):  #在运算符 * 右侧的对象是类实例

  print('nx1 / 3 = ', nx1 / 3)
  #nx1 / 3 =  3.3333333333333335
  print('nx1 / 4 = ', 4 / nx1)
  #nx1 / 4 =  2.5  #__rtruediv__(self, other): #在运算符 / 右侧的对象是类实例

  print('nx1 > 5 is ', nx1 > 5 )
  #nx1 > 5 is  True

  print('nx1 >=  15 is ', nx1 >= 15 )
  #nx1 >=  15 is  False

  print('nx1 ==  10 is ', nx1 == 10 )
  #nx1 ==  10 is  True

  print('nx1 <=  5 is ', nx1 <= 5 )
  #nx1 <=  5 is  False
  print('nx1 <  25 is ', nx1 < 25 )
  #nx1 <  25 is  True

  print('nx1 != 10 is ', nx1 != 10 )
  #nx1 != 10 is  False






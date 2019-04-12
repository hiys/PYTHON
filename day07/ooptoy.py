#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8 专门为版本2 解决默认编码问题,可以识别中文"""

import  sys

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

class  Factoryclass:
  def __init__(self, ph, email):
    self.ph = ph
    self.email = email

  def  update_ph(self, newph):
    self.ph = newph

  def  get_ph(self):
    return  self.ph

class   BearToy:

  #实例化类 产生的一个实例 默认会调用的方法__init__函数

  def  __init__(self, size, color, ph, email):
    self.size = size
    self.color = color
    self.factory = Factoryclass(ph, email)

  def   sing(self,song):    #self必不可少
    print('lalala...', song)
  
  def update_color(self, newcolor):
    self.color = newcolor
  def get_color(self):
    return  self.color

class NewBearToy(BearToy):  #在圆括号中写明从哪个父类继承
  def run(self):
    print('running ----------')
  def   sing(self):    #self必不可少,子类覆盖父的同名方法
    print('lalala...song....NewBearToy(BearToy)....')




if  __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)
  tidy = BearToy('small', 'orange', 123456, 'xixi@qq.com')
  print(tidy)
  #<__main__.BearToy object at 0x7fbd56db6320>
  print(type(tidy))
  #<class '__main__.BearToy'>
  print(tidy.size, tidy.color,sep= ' --- ')
  #small --- orange
  print(tidy.sing('hehehe'))
  #lalala... hehehe
  #None
  print('---------------')
  print(BearToy('larger','brown', 123, 'xx@qq.com'))
  #<__main__.BearToy object at 0x7f7bd14a64e0>

  print(type(BearToy('larger','brown', 123, 'xx@qq.com')))
  #<class '__main__.BearToy'>

  print(BearToy('larger','brown', 123, 'xx@qq.com').sing('newbeartoySing'))
  #lalala... newbeartoySing
  #None
  
  tidy.color = 'red'    #不推荐使用这样的用法
  print(tidy.size, tidy.color)
  #small red

  tidy.update_color('green')

  print(tidy.size, tidy.get_color())
  #small green


  tidy2 = BearToy('small', 'orange', 1234, 'hiys@163.com')

  print(tidy2.factory.get_ph())

  b1 = NewBearToy('larger','brown', 123, 'xx@qq.com')
#  b1.sing('yiyiyiyi---')
  #lalala... yiyiyiyi---
  b1.run()
  #running ----------
  b1.sing()
  #lalala...song....NewBearToy(BearToy)....
  
  print(BearToy.sing(tidy2,'sssssss---tidy2---'))  #很少使用,借用身份运行方法
  #lalala... sssssss---tidy2---
  #None
 



#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8 专门为版本2 解决默认编码问题,可以识别中文"""

import  sys

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

class   BearToy:
  #实例化类 产生的一个实例 默认会调用的方法__init__函数
  def  __init__(self, size, color):
    self.size = size
    self.color = color

  def   sing(self,song):    #self必不可少
    print('lalala...', song)
  
  def update_color(self, newcolor):
    self.color = newcolor
  def get_color(self):
    return  self.color


class NewBearToy(BearToy):  #在圆括号中写明从哪个父类继承
  def  __init__(self,size,color,material):

  #  BearToy.__init__(self, size, color)  #非绑定方法
    super(NewBearToy,self).__init__( size, color)  #非绑定方法

    self.material = material
  
  def run(self):
    print('running ----------')

class  A:
  def  fa(self):
    print('A  method')

  def  fx(self):
    print('Axx  method')
  def  fx2(self):
    print('Axx222  method')


class  B:
  def  fb(self):
    print('B  method')

  def  fx(self):
    print('Bxx  method')
  def  fx2(self):
    print('BBBBxx  method')


class  CC( A, B):  #继承自下向上,自左向右的优先顺序
  def  fc(self):
    print('CC  method')

  def  fx(self):
    print('CCxx  method')


class  D(CC):   #继承自下向上,自左向右的优先顺序
  pass


if  __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)

  b1 = NewBearToy('larger', 'brown', 'fu')
  b1.run()
  #running ----------
  b1.sing('song ------b1 --------')
  #lalala... song ------b1 --------

  c = CC()
  c.fa()
  #A  method
  c.fb()
  #B  method

  c.fc()
  #CC  method
  
  c.fx2()
  #Axx222  method

  d = D()
  d.fx()
  #CCxx  method



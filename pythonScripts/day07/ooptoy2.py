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
    super(NewBearToy,self).__init__( size, color)  #非绑定方法(实例不含self关键字)

    self.material = material   ## 被 实际 例子 绑定的属性
  
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


class  TestClass:
  count = 0    #类的属性
  class_attribute = '类的属性'

  def __init__(self):
    self.a = 10      #实例属性
    TestClass.count += 2
    self.class_attribute = self.class_attribute + '实例属性'


class  Test:
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

  print(TestClass.count)  
  #0

  mc1 = TestClass()
  print('\n------ mc1 = TestClass() -------\n', mc1.__dict__)
  #------ mc1 = TestClass() -------
  #  {'a': 10, 'class_attribute': '类的属性实例属性'}

  print(TestClass.__dict__)  
  #{  '__module__': '__main__',
#          'count': 2,
#'class_attribute': '类的属性',
#       '__init__': <function TestClass.__init__ at 0x7f1a1a6028c8>,
#       '__dict__': <attribute '__dict__' of 'TestClass' objects>,
#    '__weakref__': <attribute '__weakref__' of 'TestClass' objects>,
#        '__doc__': None}
  
  print(TestClass.count, TestClass.class_attribute)  
  # 2 类的属性

  adict = { "name" : 'peri', 'woman' : True, 'age' : 28 }
  a = Test()
  print(a.__dict__)
  #{}
  a.__dict__.update(adict)

  print(a.__dict__)
  #{'name': 'peri', 'woman': True, 'age': 28}
  print(a.age)
  #28





#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8 专门为版本2 解决默认编码问题,可以识别中文"""

import  sys
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

class  Book:
  def  __init__(self, title, author):
    "author [ˈɔ:θə(r)] n. 作者;著作家;创造者;发起人"
    self.title = title

    self.__author =  author + '隐藏属性__author'

    self.__private = '隐藏的属性__private'

    print('正在初始化 Book类实例--------\n')


  def  __str__(self):   #打印/显示实例时调用内建方法str
    return '<Book: %s>' % self.title


  def  __call__(self): #调用call内建方法可把此类型对象当作函数来使用
    print('<< %s >> is written by %s !' % (self.title, self.__author))





if  __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)
  bk = Book('Core Python', 'Wesley Chun')
  #正在初始化 Book类实例--------

  print(bk)    #自动调用方法 __str__
  #<Book: Core Python>
  bk()         #自动调用方法 __call__
  #<< Core Python >> is written by Wesley Chun隐藏属性__author !

  print("没有下划线的属性 是对外公开的属性 %s" % bk.title)
  #没有下划线的属性 是对外公开的属性 Core Python

 #访问私有属性的方式,注意是
 #"实例对象名" + "点 ." + "一个下划线 _" + 类名+ "2个下划线__" + 私有属性

  print("查看私有属性, 需要在实例对象bk的类名Book前加一个下划线, \n\
  类的后面紧接着带2个下划线的仅仅对内部共享的私有属性__private is\n\
  '%s'"  %  bk._Book__private )

  #查看私有属性, 需要在实例对象bk的类名Book前加一个下划线, 
  #  类的后面紧接着带2个下划线的仅仅对内部共享的私有属性__private is
  #  '隐藏的属性__private'



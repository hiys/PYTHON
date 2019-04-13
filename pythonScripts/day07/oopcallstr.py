#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8 专门为版本2 解决默认编码问题,可以识别中文"""

import  sys

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

class  Date:
  def __init__(self, year, month, date):  #实例化方法(绑定的方法)
    self.year = year
    self.month = month
    self.date = date
    print(year, month, date, sep = '  *  ' )


  #被 实例绑定的方法(self关键字表示绑定)
  def create_date(self, string_date):  #被实例绑定的方法(self)
    year, month, date = map(int, string_date.split('-'))
    print(year, month, date, '---create_date(self, string_date)' )


  #非绑定方法(实例方法中不含self关键字)
  def  isvalid(string_date):  # 不 被实例绑定的方法(无self)
    print(' --- isvalid(string_date) ------')
    year, month, date = map(int, string_date.split('*'))
    print(year, month, date, sep= '  *?*  ' )
    return  year < 4000 and 0 < month < 13 and 0< date < 32


  @staticmethod   #静态方法
  def  is_static(strarg):
    print('--*** is_static --- strarg is %s' % strarg )


#使用classmethod装饰器定义 创建类的方法
#(第一个 参数cls 表示类本身):
  @classmethod
  def create_date_2(cls, string_date):
    year, month, date = map(int, string_date.split('-'))
    print(year, month, date, '**create_date_2(cls, string_date)' )
    dt = cls(year, month, date)
    print(dt, type(dt),sep= ' --dt---type(dt)-- ')
    return  dt


def  is_date_valid(string_date):   #独立与类之外的方法
  year, month, date = map(int, string_date.split('-'))
  print(year, month, date,  ' *is_date_valid(string_date)' )
  return  year < 4000 and 0 < month < 13 and 0< date < 32



if  __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)

  d1 = Date(2018, 5, 19)
  #2018  *  5  *  19

  d1.create_date('2019-06-06')
  #2019 6 6 ---create_date(self, string_date)

  d2 = Date.create_date_2('2019-04-01')
  #2019 4 1 **create_date_2(cls, string_date)
  #2019  *  4  *  1
  #<__main__.Date object at 0x7f1c5a72d438> --dt---type(dt)-- <class '__main__.Date'>

  print(d2.year, d2.month, d2.date,type(d2.date))
  #2019 4 1 <class 'int'>

  print('\n------ Date.create_date(d1,"2022-02-02")------\n')
  #------ Date.create_date(d1,"2022-02-02")------

  ##很少使用,借用其他实例的身份运行方法
  print('-******- Date.create_date(d1,"2022-02-02")--\n', \
    Date.create_date(d1,'2022-02-02') )  #借用其他实例的身份运行方法

  #2022 2 2 ---create_date(self, string_date)
  #-******- Date.create_date(d1,"2022-02-02")--
  # None

  print(Date.isvalid('1023*12*13'))
  # --- isvalid(string_date) ------
  #1023  *?*  12  *?*  13
  #True

  print(is_date_valid('2022-12-33'))
  #2022 12 33  *is_date_valid(string_date)
  #False

  Date.is_static("静态方法")  #执行静态方法
  #--*** is_static --- strarg is 静态方法




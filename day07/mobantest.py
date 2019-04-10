#! /usr/bin/env python3
#coding:UTF-8
"""这是测试模版说明--------
形参名前加 2 个*表示，
参数在函数内部将被存放在以形参名
为标识符的dictionary中，
这时调用函数的方法则需要采用arg1=value1,arg2=value2这样的形式
 * 表示把序列对象（列表，字符串，元组等） 拆开，得到个体"""

import  sys, time


print('\033[31;47;1m__name__  is %s\033[0m' %  __name__)

date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())


def  get_abc(A, B, C):
  """函数方法说明: 传入 3 个参数"""
  print('\033[32;46;1m A is %s\tB is %s\t C is %s\033[0m' % (A, B, C))


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv  is %s\033[0m\n' % sys.argv) 


  infolist = [ 'peri', 33, False ]

  print("注意字典中的关键字keyword必须是字符串类型,\n \
   否则不能 通过以字典(关键字参数)作为参数组传递给函数")

  info_dict = {'keyx':'valuex', 'mustbestring':True, 'zifuchuan':['liebiao', 220]}


  get_abc(*infolist)  # *表示把序列对象(列表，字符串，元组等)拆开，得到个体元素
  # A is peri	B is 33	 C is False

  get_abc(*info_dict)  ## * 表示把字典中的 键 分解出来
  # A is keyx	B is mustbestring	 C is zifuchuan



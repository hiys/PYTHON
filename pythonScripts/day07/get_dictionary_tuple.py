#! /usr/bin/env python3
#coding=UTF-8
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


def  get_tuple(*tuple_args):  #*表示参数tuple_args 是个元组
  """argument  n.论据;[数]幅角;主题，情节
  通过以 元组(非关键字参数) 作为参数组传递给函数
  参数tuple_args 的元素个数不限制"""
  print(tuple_args, end= "  --('tuple_element',)\n")


def   get_dictionary(**dict):     # ** 两个星号表示参数dict 是个字典
  """通过以字典(关键字参数)作为参数组传递给函数"""
  print(dict,end= '  --{dictionary}\n')


def   get_dictionary_kv(**dict2):
  print(dict2)
  for k,v  in  dict2.items():  #返回可遍历的(键, 值) 元组数组
    print('k is %s  ---- v is %s' % (k,v))
  return  dict2.values()        #以列表返回字典中的所有值


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv  is %s\033[0m\n' % sys.argv) 

  get_tuple('zifuchuan', 12, True, ['lieblist','element']) #结果是个元组
  #('zifuchuan', 12, True, ['lieblist', 'element'])  --('tuple_element',)

  infolist = [ 'peri', 33, False ]

  print("注意字典中的关键字keyword必须是字符串类型,\n \
   否则不能 通过以字典(关键字参数)作为参数组传递给函数")

  info_dict = {'keyx':'valuex', 'mustbestring':True, 'zifuchuan':['liebiao', 220]}


  get_abc(*infolist)  # *表示把序列对象(列表，字符串，元组等)拆开，得到个体元素
  # A is peri	B is 33	 C is False

  get_abc(*info_dict)  ## * 表示把字典中的 键 分解出来
  # A is keyx	B is mustbestring	 C is zifuchuan


  #这时调用函数的方法则需要采用arg1=value1,arg2=value2这样的形式
  get_dictionary(name='bob', man = False ,hobby = 'music')     #结果是个字典
  #{'name': 'bob', 'man': False, 'hobby': 'music'}  --{dictionary}

  print('\n---- get_dictionary(**dict)  -----')
  

  get_dictionary(**info_dict)   # ** 两个星号表示参数info_dict 是个字典 
                                # 结果是个字典
  #{'keyx': 'valuex', 'mustbestring': True, 'zifuchuan': ['liebiao', 220]}  --{dictionary}
 

  print('\n------- get_dictionary_kv(**dict2) ---------')

  received = get_dictionary_kv(**info_dict)  #**2个星号表示参数info_dict是个字典
  #{'keyx': 'valuex', 'mustbestring': True, 'zifuchuan': ['liebiao', 220]}
  #k is keyx  ---- v is valuex
  #k is mustbestring  ---- v is True
  #k is zifuchuan  ---- v is ['liebiao', 220]


  print('get_dictionary_kv(**info_dict)返回值是\n%s \n type(received) is %s' \
       %  (received, type(received)))
  #get_dictionary_kv(**info_dict)返回值是
  #dict_values(['valuex', True, ['liebiao', 220]]) 
  # type(received) is <class 'dict_values'>



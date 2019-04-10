#!/usr/bin/env  python3
import  sys, os, pickle, time
"MoBan ------------ instruction"
print('\033[31;47;1m__name__  is %s\033[0m' %  __name__)

def  foo():
  "----- 函数\文档\字符串------"
  bar()
  print('in-foo')
  date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())
  return  date

def  bar():
  print('in-bar')
  
def  getagename(formal_parameter='first', fp2= 18, fp3= True):
  print('getagename --- first parameter is %s  second is %d  third is %s' % \
    (formal_parameter, fp2, fp3))

  def  insidex():
  #  forpar= 'firstpar'
  #  forp2, forp3 =  29, False
  #  print('inside --- first parameter is %s  second is %d  third is %s' % \
  #  (forpar, forp2, forp3))
    formal_parameter, fp2, fp3 = 'firstpar', 29, False

    print('inside --- first par is %s  second is %d  third is %s' % \
      (formal_parameter, fp2, fp3))

  insidex()


def  get_args(*args):   #*表示args 是个元组
  print(args, end=" -----('args-tuple',)\n")


def  get_argxx(*xx):   #*表示xx 是个元组
  print(xx, end=" -----('xx-tuple',)\n")


def  get_abc(a,b,c):
  print('a is %s\tb is %s\tc is %s' % (a,b,c))


#形参名前加 2 个*表示，
#参数在函数内部将被存放在以形参名
#为标识符的dictionary中，
#这时调用函数的方法则需要采用arg1=value1,arg2=value2这样的形式

def   get_dictionary(**xxx):     # ** 两个星号表示参数 xxx 是个字典
  print(xxx,end= ' -----dictionary\n')

def   get_dictionary2(**xxy):
  print(xxy)
  for k,v in xxy.items():  #返回可遍历的(键, 值) 元组数组
    print('k is %s ---- v is %s' % (k,v))
  return  xxy.values()  #以列表返回字典中的所有值



if __name__ == '__main__':
  print('\033[30;43;1m sys.argv  is %s\033[0m\n' % sys.argv)  
  foo()
    # in-bar
    # in-foo

  getagename()
     # getagename --- first parameter is first  second is 18  third is True
     # inside --- first par is firstpar  second is 29  third is False


  get_args('par1')    #结果是个元组
      #('par1',) -----('args-tuple',)

  get_args('par1',28,True,['haha','liebiao'])  ##结果是个元组
      #('par1', 28, True, ['haha', 'liebiao']) -----('args-tuple',)


  info = [ 'peri', 36, False ] #列表
  get_argxx(info)        #结果是个元组中有一个列表元素
       #(['peri', 36, False],) -----('xx-tuple',)


  get_abc(*info)  # *表示把序列对象（列表，字符串，元组等） 拆开，得到个体
     # a is peri	b is 36	c is False


  inf2 = ['lily', 18, True ]
  get_abc(*inf2)  # *表示把序列对象列表inf2 拆开，得到个体
      # a is lily	b is 18	c is True


#这时调用函数的方法则需要采用arg1=value1,arg2=value2这样的形式
  get_dictionary(name='bob',gender= 1 ,hobby = True)
    # {'name': 'bob', 'gender': 1, 'hobby': True} -----dictionary

  info3 = {'xx1' : 'valuex1', 'girl' : False, 'name' : 'beauty' }

  get_abc(*info3)    # * 表示把字典中的 键 分解出来
     #a is xx1	b is girl	c is name

  get_dictionary(**info3)
   #{'xx1': 'valuex1', 'girl': False, 'name': 'beauty'} -----dictionary

  dictxobj = get_dictionary(**info3)
     #{'xx1': 'valuex1', 'girl': False, 'name': 'beauty'} -----dictionary


  print(type(dictxobj), end= '  --type(dictxobj\n')
     #<class 'NoneType'>  --type(dictxobj

  print(dictxobj)
     #None

  get_dictionary2(**info3) # ** 表示把字典中的 键值 分解出来
     #{'xx1': 'valuex1', 'girl': False, 'name': 'beauty'}
     #k is xx1 ---- v is valuex1
     #k is girl ---- v is False
     #k is name ---- v is beauty


  


#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
compile      v.编写(书、列表、报告等) ; 编译
re.compile()函数 对正则表达式模式进行编译,返回一个正则表达式对象
>>> sre_p = re.compile('^-?\d+\.\d+$')
>>> type(sre_p)    #正则表达式对象sre_p
<class '_sre.SRE_Pattern'>
>>> sre_p
re.compile('^-?\\d+\\.\\d+$')

re.match() 函数  用正则表达式模式从字符串的 开头位置 开始匹配
re.search()函数 #如果匹配成功,则返回一个匹配对象SRE_Match object
•  在字符串中查找正则表达式模式的第一次出现
>>> sre_p.search('-12.314')
<_sre.SRE_Match object; span=(0, 7), match='-12.314'>

>>> sre_p.search('-12.314').group()
'-12.314'
>>> sre_p.search('-12.314').groups()
()
>>> countx = collections.Counter('abc23abAAbb')
>>> countx         #计数器对象countx
Counter({'b': 4, 'a': 2, 'A': 2, 'c': 1, '2': 1, '3': 1})
>>> type(countx)
<class 'collections.Counter'>
>>> countx['a']
2
>>> countx = collections.Counter(['AAbb'])
>>> countx
Counter({'AAbb': 1})
>>> type(countx)
<class 'collections.Counter'>

>>> addstr = 'AAbb'
>>> 
>>> countx.update([addstr])  #注意把变量存进列表里,就不会拆开字符串了

>>> countx
Counter({'AAbb': 2})

>>> addstr = 1234
>>> countx.update([addstr])

>>> countx
Counter({'AAbb': 2, 1234: 1})
>>> 
"""

import  sys, socket, time, collections, re

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())


#/root/pyscripts/day08/testapache.txt
#-rw-r--r-- 1 root root 623 4月  17 16:17 /root/pyscripts/day08/testapache.txt
#pattern  模式, 范例
#fname  文件地址   patt  正则表达式

#创建类CountPatt(object)
class  CountPatt(object):
  #定义构造方法 创建正则表达式对象cpatt实例
  def  __init__(self, patt):
    self.cpatt = re.compile(patt)

  #定义类的方法
  def  count_patt(self, fname):
    #创建计数器对象
    counter = collections.Counter()  # 计数器对象counter实例
    #打开文件
    with  open(fname)  as  fobj:
      for  line  in  fobj:      #遍历
      ##如果匹配成功,则返回一个匹配对象SRE_Match object类实例m
        m = self.cpatt.search(line)  #通过正则表达式对象cpatt实例查找匹配的字符串
        print(m, end ='\n\n')
        if m:
          print(m.group())
## counter.update()函数更新原来的字符串,相同的键的值会累积追加计算#更新计数器
                     # group() 方法获得匹配内容
          counter.update([m.group()]) #注意把m.group()返回结果存进列表里,就不会拆开字符串了
          print(counter)
    return counter    #返回 计数器对象counter实例




if  __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)
  fname = "/root/pyscripts/day08/testapache.txt"
  ip_patt = "^(\d+\.){3}\d+"
  aip = CountPatt(ip_patt)
  print(type(aip),aip, sep ='\n',end = '---END\n\n')
  
  print(aip.count_patt(fname))

  print('\n-------browser = CountPatt(br_patt)--------\n')

  br_patt = "ELinks|Mozilla|Chrome"
  browser = CountPatt(br_patt)
  print(type(browser),browser, sep ='\n',end = '---END\n')

  print(browser.count_patt(fname))




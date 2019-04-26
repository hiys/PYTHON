#!/usr/bin/env python3
#coding:UTF-8
"""#coding=UTF-8
constraint    英 [kənˈstreɪnt] 
       n.限制;限定;约束;严管
row    英 [rəʊ , raʊ]
n.一排;一列;一行;(剧院、电影院等的)一排座位;(编织中的)针行，一整行
https://yiyibooks.cn/?search=sqlalchemy中文翻译文档
https://yiyibooks.cn/information/wizard/sqlalchemy_11/
https://yiyibooks.cn/wizard/sqlalchemy_11/index.html
alchemy       美 [ˈælkəmi]  
       n.炼金术, 神秘力量，魔力

句柄（handle），有多种意义，其中第一种是指程序设计，第二种是指Windows编程。
第一种解释：句柄是一种特殊的智能指针 。
当一个应用程序要引用其他系统（如数据库、操作系统）所管理的内存块或对象时，就要使用句柄。

第二种解释：整个Windows编程的基础。
一个句柄是指使用的一个唯一的整数值，即一个4字节(64位程序中为8字节)长的数值，
来标识应用程序中的不同对象和同类中的不同的实例

ORM即对象关系映射
对象关系映射器（Object Relational Mappers，ORM）
就是在python中设定一个类，
在mysql中定义一个表，
把关系数据库的表结构映射到这个类上
>>> import   collections
>>> help(collections)
.........
/named  #输入named 搜索

FUNCTIONS
    namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
        Returns a new subclass of tuple with named fields.
(END)
>>>
element    英 [ˈelɪmənt]
   n.要素;基本部分;典型部分;
  >>> Point = namedtuple('Point', ['x', 'y'])

>>> tuple_element= collections.namedtuple('tuple_element', ['index0', 'index_1'])

>>> tuple_element.__doc__
'tuple_element(index0, index_1)'

>>> peri = tuple_element('red peri', 18)

>>> type(peri)
<class '__main__.tuple_element'>

>>> peri
tuple_element(index0='red peri', index_1=18)

>>> peri[0]
'red peri'
>>> type(peri[0])
<class 'str'>
>>> peri[1]
18
>>> peri.index0
'red peri'
>>> peri.index_1
18
>>> 
AttributeError: 'Query' object has no attribute 'dep_id'
"""

import  sys,  subprocess
from  alchemy_ORM  import  Departments, Employees, Salary, session
from  sqlalchemy   import  and_,  or_

q = session.query(Departments)
print('\n------type(q)= %s\n----- q = %s -----\n' % (type(q), q))
#------type(q)= <class 'sqlalchemy.orm.query.Query'>
#----- q = SELECT departments.dep_id AS departments_dep_id, departments.dep_name AS departments_dep_name 
#FROM departments -----


print('\n------ %s --------\n' % q.all())
#------ [<alchemy_ORM.Departments object at 0x7f7b4751ff60>, <alchemy_ORM.Departments object at 0x7f7b4751ffd0>, <alchemy_ORM.Departments object at 0x7f7b471e6978>, <alchemy_ORM.Departments object at 0x7f7b471e6198>] --------


print('\n-------------------- %s : %s ------------------\n')
for  row  in  q :
  print('-------- %s : %s --------' % (row.dep_id, row.dep_name))
#-------- 1 : 人力部 --------
#-------- 2 : 开发部 --------
#-------- 4 : 财务部 --------
#-------- 3 : 运维部 --------

#搜索部门名称等于'人力部'  的记录-----------
q = session.query(Departments).filter(Departments.dep_name=='人力部')
print('\n------type(q)= %s\n----- q = %s -----\n' % (type(q), q))
#------type(q)= <class 'sqlalchemy.orm.query.Query'>
#----- q = SELECT departments.dep_id AS departments_dep_id, departments.dep_name AS departments_dep_name 
#FROM departments 
#WHERE departments.dep_name = %(dep_name_1)s -----


#[root@V0 devops_day02]# mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy -e "
#> SELECT departments.dep_id , departments.dep_name
#> FROM departments 
#> WHERE departments.dep_name = '人力部';" 
#+--------+-----------+
#| dep_id | dep_name  |
#+--------+-----------+
#|      1 | 人力部    |
#+--------+-----------+

#all()返回列表
print('\n------ %s --------\n' % q.all())
#2019-04-25 18:42:02,761 INFO sqlalchemy.engine.base.Engine {'dep_name_1': '人力部'}

#------ [<alchemy_ORM.Departments object at 0x7f15f969feb8>] --------

for  row  in  q :
  print('-------- %s : %s --------' % (row.dep_id, row.dep_name))
#-------- 1 : 人力部 --------

q.update({Departments.dep_name : '人力资源部'})  #更新部门名称

session.commit()


#搜索部门名称等于'人力资源部'  的记录-----------

q = session.query(Departments).filter(Departments.dep_name=='人力资源部')

for  row  in  q :
  print('-------- %s : %s --------' % (row.dep_id, row.dep_name))
#-------- 1 : 人力资源部 --------


sqlcmd = "\"\
SELECT departments.dep_id , departments.dep_name  \
FROM departments  \
WHERE departments.dep_name = '人力资源部';\""

mysqlshell= "mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  %s" %  sqlcmd

print('------------------------------')
print(mysqlshell)
print('------------------------------')
#------------------------------
#mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  "SELECT departments.dep_id , departments.dep_name  FROM departments  WHERE departments.dep_name = '人力资源部';"
#------------------------------

rcmd = subprocess.call(mysqlshell, shell = True)
  
if rcmd == 0:
  print('-----OK ---- rcmd  --------\n')
else:
  print('----- rcmd = %d -------\n' % rcmd)
#+--------+-----------------+
#| dep_id | dep_name        |
#+--------+-----------------+
#|      1 | 人力资源部      |
#+--------+-----------------+
#-----OK ---- rcmd  --------

q.update({Departments.dep_name : '人力部'})   #更新部门名称

session.commit()


sqlcmd = "\"\
SELECT departments.dep_id , departments.dep_name  \
FROM departments  \
WHERE departments.dep_name = '人力部';\""

mysqlshell= 'mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  %s' %  sqlcmd


print('\n------------------------------')
print(mysqlshell)
print('------------------------------\n')
#------------------------------
#mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  "SELECT departments.dep_id , departments.dep_name  FROM departments  WHERE departments.dep_name = '人力部';"
#------------------------------

print('\n---- ======= 查看 \'人力部\' ===== ------\n')

rcmd2 = subprocess.call(mysqlshell, shell = True)

if rcmd2 == 0:
  print('-----OK ---- rcmd2  --------\n')
else:
  print('----- rcmd2 = %d -------\n' % rcmd2)
#+--------+-----------+
#| dep_id | dep_name  |
#+--------+-----------+
#|      1 | 人力部    |
#+--------+-----------+
#-----OK ---- rcmd2  --------


print('\n---- ===== 把\'人力部\' 改成 人力资源部 ====== ------\n')

#返回的是一个 Departments类的实例 q, 
q = session.query(Departments).get(1)  ##get(1)查询主键是1的记录

#打印实例q 会默认调用内建方法__str__(self)
print('\n------type(q)= %s\n----- q = %s -----\n' % (type(q), q))
#------type(q)= <class 'alchemy_ORM.Departments'>
#----- q = <Departments(dep_name= 人力部)> -----

q.dep_name = '人力资源部'  #更新部门名称

session.commit()  #提交请求

print('\n---- ======= 查看 \'人力资源部\' ===== ------\n')

sqlcmd = "\"\
SELECT departments.dep_id , departments.dep_name  \
FROM departments  \
WHERE departments.dep_name = '人力资源部';\""

mysqlshell= 'mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  %s' %  sqlcmd

rcmd3 = subprocess.call(mysqlshell, shell = True)

if rcmd3 == 0:
  print('-----OK ---- rcmd3  --------\n')
else:
  print('----- rcmd3 = %d -------\n' % rcmd3)
#+--------+-----------------+
#| dep_id | dep_name        |
#+--------+-----------------+
#|      1 | 人力资源部      |
#+--------+-----------------+
#-----OK ---- rcmd3  --------


print('\n---- ======= 把\'人力资源部\'  改回 \'人力部\'===== ------\n')

sqlcmd = "\"\
UPDATE departments SET dep_name= '人力部'  \
WHERE departments.dep_name = '人力资源部';\""

mysqlshell= 'mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  %s' %  sqlcmd

rcmd3 = subprocess.call(mysqlshell, shell = True)

if rcmd3 == 0:
  print('-----OK ---- rcmd3  --------\n')
else:
  print('----- rcmd3 = %d -------\n' % rcmd3)





if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])









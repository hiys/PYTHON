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

#q = session.query(Departments)
#
#print('\n------ %s --------\n' % q.all())
##------ [<alchemy_ORM.Departments object at 0x7f7b4751ff60>, <alchemy_ORM.Departments object at 0x7f7b4751ffd0>, <alchemy_ORM.Departments object at 0x7f7b471e6978>, <alchemy_ORM.Departments object at 0x7f7b471e6198>] --------
#
#for  row  in  q :
#  print('-------- %s : %s --------' % (row.dep_id, row.dep_name))
##-------- 1 : 人力部 --------
##-------- 2 : 开发部 --------
##-------- 4 : 财务部 --------
##-------- 3 : 运维部 --------
#
##搜索部门名称等于'人力部'  的记录-----------
#q = session.query(Departments).filter(Departments.dep_name=='人力部')
#
##all()返回列表
#print('\n------ %s --------\n' % q.all())
##2019-04-25 18:42:02,761 INFO sqlalchemy.engine.base.Engine {'dep_name_1': '人力部'}
#
##------ [<alchemy_ORM.Departments object at 0x7f15f969feb8>] --------
#
#for  row  in  q :
#  print('-------- %s : %s --------' % (row.dep_id, row.dep_name))
##-------- 1 : 人力部 --------
#
#q.update({Departments.dep_name : '人力资源部'})  #更新部门名称
#
#session.commit()
#
#
##搜索部门名称等于'人力资源部'  的记录-----------
#
#q = session.query(Departments).filter(Departments.dep_name=='人力资源部')
#
#for  row  in  q :
#  print('-------- %s : %s --------' % (row.dep_id, row.dep_name))
##-------- 1 : 人力资源部 --------
#
#
#sqlcmd = "\"\
#SELECT departments.dep_id , departments.dep_name  \
#FROM departments  \
#WHERE departments.dep_name = '人力资源部';\""
#
#mysqlshell= "mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  %s" %  sqlcmd
#
#print('------------------------------')
#print(mysqlshell)
#print('------------------------------')
##------------------------------
##mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  "SELECT departments.dep_id , departments.dep_name  FROM departments  WHERE departments.dep_name = '人力资源部';"
##------------------------------
#
#rcmd = subprocess.call(mysqlshell, shell = True)
#  
#if rcmd == 0:
#  print('-----OK ---- rcmd  --------\n')
#else:
#  print('----- rcmd = %d -------\n' % rcmd2)
##+--------+-----------------+
##| dep_id | dep_name        |
##+--------+-----------------+
##|      1 | 人力资源部      |
##+--------+-----------------+
##-----OK ---- rcmd  --------
#
#q.update({Departments.dep_name : '人力部'})   #更新部门名称
#
#session.commit()
#
#
#sqlcmd = "\"\
#SELECT departments.dep_id , departments.dep_name  \
#FROM departments  \
#WHERE departments.dep_name = '人力部';\""
#
#mysqlshell= 'mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  %s' %  sqlcmd
#
#
#print('\n------------------------------')
#print(mysqlshell)
#print('------------------------------\n')
##------------------------------
##mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  "SELECT departments.dep_id , departments.dep_name  FROM departments  WHERE departments.dep_name = '人力部';"
##------------------------------
#
#print('\n---- ======= 查看 \'人力部\' ===== ------\n')
#
#rcmd2 = subprocess.call(mysqlshell, shell = True)
#
#if rcmd2 == 0:
#  print('-----OK ---- rcmd2  --------\n')
#else:
#  print('----- rcmd2 = %d -------\n' % rcmd2)
##+--------+-----------+
##| dep_id | dep_name  |
##+--------+-----------+
##|      1 | 人力部    |
##+--------+-----------+
##-----OK ---- rcmd2  --------
#
#
#print('\n---- ===== 把\'人力部\' 改成 人力资源部 ====== ------\n')
#
##返回的是一个 Departments类的实例 q, 
#q = session.query(Departments).get(1)  ##get(1)查询主键是1的记录
#
##打印实例q 会默认调用内建方法__str__(self)
#print('\n------type(q)= %s\n----- q = %s -----\n' % (type(q), q))
##------type(q)= <class 'alchemy_ORM.Departments'>
##----- q = <Departments(dep_name= 人力部)> -----
#
#q.dep_name = '人力资源部'  #更新部门名称
#
#session.commit()  #提交请求
#
#print('\n---- ======= 查看 \'人力资源部\' ===== ------\n')
#
#sqlcmd = "\"\
#SELECT departments.dep_id , departments.dep_name  \
#FROM departments  \
#WHERE departments.dep_name = '人力资源部';\""
#
#mysqlshell= 'mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  %s' %  sqlcmd
#
#rcmd3 = subprocess.call(mysqlshell, shell = True)
#
#if rcmd3 == 0:
#  print('-----OK ---- rcmd3  --------\n')
#else:
#  print('----- rcmd3 = %d -------\n' % rcmd3)
##+--------+-----------------+
##| dep_id | dep_name        |
##+--------+-----------------+
##|      1 | 人力资源部      |
##+--------+-----------------+
##-----OK ---- rcmd3  --------
#
#
#print('\n---- ======= 把\'人力资源部\'  改回 \'人力部\'===== ------\n')
#
#sqlcmd = "\"\
#UPDATE departments SET dep_name= '人力部'  \
#WHERE departments.dep_name = '人力资源部';\""
#
#mysqlshell= 'mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  %s' %  sqlcmd
#
#rcmd3 = subprocess.call(mysqlshell, shell = True)
#
#if rcmd3 == 0:
#  print('-----OK ---- rcmd3  --------\n')
#else:
#  print('----- rcmd3 = %d -------\n' % rcmd3)


sqlcmd = "\"\
SELECT *  \
FROM  employees;\""

mysqlshell= "mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  %s" %  sqlcmd

print('------------------------------')
print(mysqlshell)
print('------------------------------')
#------------------------------
#mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  "SELECT *  FROM  employees;"
#------------------------------

rcmd = subprocess.call(mysqlshell, shell = True)
  
if rcmd == 0:
  print('-----OK ---- rcmd  --------\n')
else:
  print('----- rcmd = %d -------\n' % rcmd)

#+--------+----------+--------+-------------+----------------+--------+
#| emp_id | emp_name | gender | phone       | email          | dep_id |
#+--------+----------+--------+-------------+----------------+--------+
#|      1 | bob      | male   | 13302381238 | bob@qq.com     |      1 |
#|      2 | alice    | female | 15802381238 | alice@qq.com   |      1 |
#|      3 | 张三     | male   | 15802581238 | zs@qq.com      |      1 |
#|      4 | 李四     | male   | 13305881255 | lisi@qq.com    |      2 |
#|      5 | 王五     | male   | 13302381238 | ww@qq.com      |      2 |
#|      6 | 赵六     | female | 13502381258 | zhaoliu@qq.com |      3 |
#|      7 | peri     | female | 15802381258 | peri@qq.com    |      4 |
#|      8 | 老八     | male   | NULL        | NULL           |      4 |
#|      9 | 九妹     | female | NULL        | sister@qq.com  |      4 |
#+--------+----------+--------+-------------+----------------+--------+
#-----OK ---- rcmd  --------


##搜索员工id号等于 8 的记录-----
#返回的是一个 Employees类的实例 q,
q = session.query(Employees).get(8)

#打印实例q 会默认调用内建方法__str__(self)
print('\n---- q = %s   type(q)= %s ----------------\n' % (q, type(q)))
#---- q = <Employees(emp_name= 老八)>   type(q)= <class 'alchemy_ORM.Employees'> ----------------

session.delete(q)  #删除这条记录

session.commit()   ##提交请求

print('\n-----已经删除emp_id= 8的数据| 老八 | male | NULL  | NULL | 4 |---\n')

sqlcmd = "\"\
SELECT *  \
FROM  employees;\""
mysqlshell= "mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  %s" %  sqlcmd
print('------------------------------')
print(mysqlshell)
print('------------------------------')
#------------------------------
#mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  "SELECT *  FROM  employees;"
#------------------------------

rcmd = subprocess.call(mysqlshell, shell = True)

if rcmd == 0:
  print('-----OK ---- rcmd  --------\n')
else:
  print('----- rcmd = %d -------\n' % rcmd)
#+--------+----------+--------+-------------+----------------+--------+
#| emp_id | emp_name | gender | phone       | email          | dep_id |
#+--------+----------+--------+-------------+----------------+--------+
#|      1 | bob      | male   | 13302381238 | bob@qq.com     |      1 |
#|      2 | alice    | female | 15802381238 | alice@qq.com   |      1 |
#|      3 | 张三     | male   | 15802581238 | zs@qq.com      |      1 |
#|      4 | 李四     | male   | 13305881255 | lisi@qq.com    |      2 |
#|      5 | 王五     | male   | 13302381238 | ww@qq.com      |      2 |
#|      6 | 赵六     | female | 13502381258 | zhaoliu@qq.com |      3 |
#|      7 | peri     | female | 15802381258 | peri@qq.com    |      4 |
#|      9 | 九妹     | female | NULL        | sister@qq.com  |      4 |
#+--------+----------+--------+-------------+----------------+--------+
#-----OK ---- rcmd  --------


##搜索员工id号等于 9 的记录-----
#返回的是一个 Employees类的实例 q,

q = session.query(Employees).get(9)

#打印实例q 会默认调用内建方法__str__(self)
print('\n---- q = %s -------\n' % q )
#---- q = <Employees(emp_name= 九妹)> -------

q.emp_id= 8  #更新员工号


session.commit()  #提交请求


session.close()

print('\n-----已经修改更新emp_id= 9的记录 为 emp_id= 8 ---\n')

sqlcmd = "\"\
SELECT *  \
FROM  employees;\""
mysqlshell= "mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  %s" %  sqlcmd
print('------------------------------')
print(mysqlshell)
print('------------------------------')
#------------------------------
#mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  "SELECT *  FROM  employees;"
#------------------------------

rcmd = subprocess.call(mysqlshell, shell = True)

if rcmd == 0:
  print('-----OK ---- rcmd  --------\n')
else:
  print('----- rcmd = %d -------\n' % rcmd)

#+--------+----------+--------+-------------+----------------+--------+
#| emp_id | emp_name | gender | phone       | email          | dep_id |
#+--------+----------+--------+-------------+----------------+--------+
#|      1 | bob      | male   | 13302381238 | bob@qq.com     |      1 |
#|      2 | alice    | female | 15802381238 | alice@qq.com   |      1 |
#|      3 | 张三     | male   | 15802581238 | zs@qq.com      |      1 |
#|      4 | 李四     | male   | 13305881255 | lisi@qq.com    |      2 |
#|      5 | 王五     | male   | 13302381238 | ww@qq.com      |      2 |
#|      6 | 赵六     | female | 13502381258 | zhaoliu@qq.com |      3 |
#|      7 | peri     | female | 15802381258 | peri@qq.com    |      4 |
#|      8 | 九妹     | female | NULL        | sister@qq.com  |      4 |
#+--------+----------+--------+-------------+----------------+--------+
#-----OK ---- rcmd  --------




if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])



#[root@V0 devops_day02]# python3   alchemy_delete.py
#__name__ is alchemy_ORM
#type(enginex) = <class 'sqlalchemy.engine.base.Engine'>,  enginex = Engine(mysql+pymysql://root:***@192.168.1.11/alchemy?charset=utf8)
#
#Base.metadata.create_all = <bound method MetaData.create_all of MetaData(bind=None)>, type(Base.metadata.create_all)= <class 'method'>
#
#Sessionmk = sessionmaker(class_='Session', bind=None, autoflush=True, autocommit=False, expire_on_commit=True),  type(Sessionmk)= <class 'sqlalchemy.orm.session.sessionmaker'>
#
#session = <sqlalchemy.orm.session.Session object at 0x7fc012fa43c8>,  type(session)= <class 'sqlalchemy.orm.session.Session'>
#
#------------------------------
#mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  "SELECT *  FROM  employees;"
#------------------------------
#+--------+----------+--------+-------------+----------------+--------+
#| emp_id | emp_name | gender | phone       | email          | dep_id |
#+--------+----------+--------+-------------+----------------+--------+
#|      1 | bob      | male   | 13302381238 | bob@qq.com     |      1 |
#|      2 | alice    | female | 15802381238 | alice@qq.com   |      1 |
#|      3 | 张三     | male   | 15802581238 | zs@qq.com      |      1 |
#|      4 | 李四     | male   | 13305881255 | lisi@qq.com    |      2 |
#|      5 | 王五     | male   | 13302381238 | ww@qq.com      |      2 |
#|      6 | 赵六     | female | 13502381258 | zhaoliu@qq.com |      3 |
#|      7 | peri     | female | 15802381258 | peri@qq.com    |      4 |
#|      8 | 老八     | male   | NULL        | NULL           |      4 |
#|      9 | 九妹     | female | NULL        | sister@qq.com  |      4 |
#+--------+----------+--------+-------------+----------------+--------+
#-----OK ---- rcmd  --------
#
#2019-04-26 11:53:29,145 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'sql_mode'
#2019-04-26 11:53:29,146 INFO sqlalchemy.engine.base.Engine {}
#2019-04-26 11:53:29,146 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
#2019-04-26 11:53:29,146 INFO sqlalchemy.engine.base.Engine {}
#2019-04-26 11:53:29,147 INFO sqlalchemy.engine.base.Engine SELECT DATABASE()
#2019-04-26 11:53:29,147 INFO sqlalchemy.engine.base.Engine {}
#2019-04-26 11:53:29,148 INFO sqlalchemy.engine.base.Engine show collation where `Charset` = 'utf8mb4' and `Collation` = 'utf8mb4_bin'
#2019-04-26 11:53:29,148 INFO sqlalchemy.engine.base.Engine {}
#2019-04-26 11:53:29,149 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS CHAR(60)) AS anon_1
#2019-04-26 11:53:29,150 INFO sqlalchemy.engine.base.Engine {}
#2019-04-26 11:53:29,150 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS CHAR(60)) AS anon_1
#2019-04-26 11:53:29,150 INFO sqlalchemy.engine.base.Engine {}
#2019-04-26 11:53:29,151 INFO sqlalchemy.engine.base.Engine SELECT CAST('test collated returns' AS CHAR CHARACTER SET utf8mb4) COLLATE utf8mb4_bin AS anon_1
#2019-04-26 11:53:29,151 INFO sqlalchemy.engine.base.Engine {}
#2019-04-26 11:53:29,152 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
#2019-04-26 11:53:29,153 INFO sqlalchemy.engine.base.Engine SELECT employees.emp_id AS employees_emp_id, employees.emp_name AS employees_emp_name, employees.gender AS employees_gender, employees.phone AS employees_phone, employees.email AS employees_email, employees.dep_id AS employees_dep_id 
#FROM employees 
#WHERE employees.emp_id = %(param_1)s
#2019-04-26 11:53:29,153 INFO sqlalchemy.engine.base.Engine {'param_1': 8}
#
#---- q = <Employees(emp_name= 老八)>   type(q)= <class 'alchemy_ORM.Employees'> ----------------
#
#2019-04-26 11:53:29,154 INFO sqlalchemy.engine.base.Engine DELETE FROM employees WHERE employees.emp_id = %(emp_id)s
#2019-04-26 11:53:29,154 INFO sqlalchemy.engine.base.Engine {'emp_id': 8}
#2019-04-26 11:53:29,155 INFO sqlalchemy.engine.base.Engine COMMIT
#
#-----已经删除emp_id= 8的数据| 老八 | male | NULL  | NULL | 4 |---
#
#------------------------------
#mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  "SELECT *  FROM  employees;"
#------------------------------
#+--------+----------+--------+-------------+----------------+--------+
#| emp_id | emp_name | gender | phone       | email          | dep_id |
#+--------+----------+--------+-------------+----------------+--------+
#|      1 | bob      | male   | 13302381238 | bob@qq.com     |      1 |
#|      2 | alice    | female | 15802381238 | alice@qq.com   |      1 |
#|      3 | 张三     | male   | 15802581238 | zs@qq.com      |      1 |
#|      4 | 李四     | male   | 13305881255 | lisi@qq.com    |      2 |
#|      5 | 王五     | male   | 13302381238 | ww@qq.com      |      2 |
#|      6 | 赵六     | female | 13502381258 | zhaoliu@qq.com |      3 |
#|      7 | peri     | female | 15802381258 | peri@qq.com    |      4 |
#|      9 | 九妹     | female | NULL        | sister@qq.com  |      4 |
#+--------+----------+--------+-------------+----------------+--------+
#-----OK ---- rcmd  --------
#
#2019-04-26 11:53:29,172 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
#2019-04-26 11:53:29,173 INFO sqlalchemy.engine.base.Engine SELECT employees.emp_id AS employees_emp_id, employees.emp_name AS employees_emp_name, employees.gender AS employees_gender, employees.phone AS employees_phone, employees.email AS employees_email, employees.dep_id AS employees_dep_id 
#FROM employees 
#WHERE employees.emp_id = %(param_1)s
#2019-04-26 11:53:29,173 INFO sqlalchemy.engine.base.Engine {'param_1': 9}
#
#---- q = <Employees(emp_name= 九妹)> -------
#
#2019-04-26 11:53:29,174 INFO sqlalchemy.engine.base.Engine UPDATE employees SET emp_id=%(emp_id)s WHERE employees.emp_id = %(employees_emp_id)s
#2019-04-26 11:53:29,174 INFO sqlalchemy.engine.base.Engine {'emp_id': 8, 'employees_emp_id': 9}
#2019-04-26 11:53:29,175 INFO sqlalchemy.engine.base.Engine COMMIT
#
#-----已经修改更新emp_id= 9的记录 为 emp_id= 8 ---
#
#------------------------------
#mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  "SELECT *  FROM  employees;"
#------------------------------
#+--------+----------+--------+-------------+----------------+--------+
#| emp_id | emp_name | gender | phone       | email          | dep_id |
#+--------+----------+--------+-------------+----------------+--------+
#|      1 | bob      | male   | 13302381238 | bob@qq.com     |      1 |
#|      2 | alice    | female | 15802381238 | alice@qq.com   |      1 |
#|      3 | 张三     | male   | 15802581238 | zs@qq.com      |      1 |
#|      4 | 李四     | male   | 13305881255 | lisi@qq.com    |      2 |
#|      5 | 王五     | male   | 13302381238 | ww@qq.com      |      2 |
#|      6 | 赵六     | female | 13502381258 | zhaoliu@qq.com |      3 |
#|      7 | peri     | female | 15802381258 | peri@qq.com    |      4 |
#|      8 | 九妹     | female | NULL        | sister@qq.com  |      4 |
#+--------+----------+--------+-------------+----------------+--------+
#-----OK ---- rcmd  --------
#
# sys.argv[0]  is alchemy_delete.py
#
#[root@V0 devops_day02]# 






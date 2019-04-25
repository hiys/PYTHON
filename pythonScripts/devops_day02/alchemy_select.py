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
"""

import  sys,  subprocess
from  alchemy_ORM  import  Departments, Employees, Salary, session
from  sqlalchemy   import  and_,  or_

#通过作用于session的query()函数创建查询对象
#select * from  departments order by dep_id;
for  instance  in  session.query(Departments).order_by(Departments.dep_id):
  print(instance)
  print(instance.dep_id, ':', instance.dep_name)
#2019-04-25 11:53:43,245 INFO sqlalchemy.engine.base.Engine
# SELECT departments.dep_id AS departments_dep_id, departments.dep_name AS departments_dep_name 
#FROM departments ORDER BY departments.dep_id
#2019-04-25 11:53:43,245 INFO sqlalchemy.engine.base.Engine {}
#<Departments(dep_name= 人力部)>
#1 : 人力部
#<Departments(dep_name= 开发部)>
#2 : 开发部
#<Departments(dep_name= 运维部)>
#3 : 运维部
#<Departments(dep_name= 财务部)>
#4 : 财务部

#使用ORM描述符进行查询,返回值是元组

for  i  in  session.query(Employees.emp_name, Employees.phone):
  print('i= %s, type(i)= %s,\n%s:%s' % (i, type(i), i[0], i[1]))
#2019-04-25 12:08:05,156 INFO sqlalchemy.engine.base.Engine
# SELECT employees.emp_name AS employees_emp_name, employees.phone AS employees_phone 
#FROM employees
#2019-04-25 12:08:05,156 INFO sqlalchemy.engine.base.Engine {}
#i= ('bob', '13302381238'), type(i)= <class 'sqlalchemy.util._collections.result'>,
#bob:13302381238
#i= ('alice', '15802381238'), type(i)= <class 'sqlalchemy.util._collections.result'>,
#alice:15802381238
#i= ('张三', '15802581238'), type(i)= <class 'sqlalchemy.util._collections.result'>,
#张三:15802581238
#i= ('李四', '13305881255'), type(i)= <class 'sqlalchemy.util._collections.result'>,
#李四:13305881255
#i= ('王五', '13302381238'), type(i)= <class 'sqlalchemy.util._collections.result'>,
#王五:13302381238
#i= ('赵六', '13502381258'), type(i)= <class 'sqlalchemy.util._collections.result'>,
#赵六:13502381258
#i= ('peri', '15802381258'), type(i)= <class 'sqlalchemy.util._collections.result'>,
#peri:15802381258


#使用ORM描述符进行查询,返回值是元组
#使用命名元组
#查询对象返回的是一个命名元组
#>>> import   collections
#>>> tuple_element= collections.namedtuple('tuple_element', ['index0', 'index_1'])
#>>> peri = tuple_element('red peri', 18)
#>>> peri
#tuple_element(index0='red peri', index_1=18)
#>>> peri[0]
#'red peri'
#>>> peri[1]
#18
#>>> peri.index0
#'red peri'
#>>> peri.index_1
#18
#>>> 
for  row  in  session.query(Departments.dep_id, Departments.dep_name):
  print('row= %s, %s:%s' % (i, row.dep_id, row.dep_name))
#row= ('peri', '15802381258'), 1:人力部
#row= ('peri', '15802381258'), 2:开发部
#row= ('peri', '15802381258'), 4:财务部
#row= ('peri', '15802381258'), 3:运维部

print(session.query(Departments))
#SELECT departments.dep_id AS departments_dep_id, departments.dep_name AS departments_dep_name 
#FROM departments
print(type(session.query(Departments)))
#<class 'sqlalchemy.orm.query.Query'>

for  row  in  session.query(Departments, Departments.dep_name.label('as部门')):
  print(row, row.as部门,sep= ' ----- ')
#(<alchemy_ORM.Departments object at 0x7f0eb2717278>, '人力部') ----- 人力部
#(<alchemy_ORM.Departments object at 0x7f0eb27176a0>, '开发部') ----- 开发部
#(<alchemy_ORM.Departments object at 0x7f0eb27171d0>, '财务部') ----- 财务部
#(<alchemy_ORM.Departments object at 0x7f0eb2717a20>, '运维部') ----- 运维部

print(session.query(Departments, Departments.dep_name.label('as部门')))
#SELECT departments.dep_id AS departments_dep_id, departments.dep_name AS departments_dep_name, departments.dep_name AS `as部门` 
#FROM departments

print('================ -------------------------')
for  row  in  session.query(Departments):
  print(row.dep_id, row.dep_name)
#1 人力部
#2 开发部
#4 财务部
#3 运维部
for  row  in  session.query(Departments).order_by(Departments.dep_id):
  print('--- %s : %s' %  (row.dep_id, row.dep_name))
#--- 1 : 人力部
#--- 2 : 开发部
#--- 3 : 运维部
#--- 4 : 财务部

#.order_by(Departments.dep_id.desc()):
#注意降序排列.desc()
for  row  in  session.query(Departments).order_by(Departments.dep_id.desc()):
  print('#--- %s : %s' %  (row.dep_id, row.dep_name))
#--- 4 : 财务部
#--- 3 : 运维部
#--- 2 : 开发部
#--- 1 : 人力部

#SELECT departments.dep_id AS departments_dep_id, departments.dep_name AS departments_dep_name 
#FROM departments ORDER BY departments.dep_id 
# LIMIT %(param_1)s, %(param_2)s
for  row  in  session.query(Departments).order_by(Departments.dep_id)[1:3]:
  print('#------ %s : %s' %  (row.dep_id, row.dep_name))
#------ 2 : 开发部
#------ 3 : 运维部
#[root@V0 devops_day02]# mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy -e "
#select  *  from  departments order by dep_id limit 1, 2;"
#+--------+-----------+
#| dep_id | dep_name  |
#+--------+-----------+
#|      2 | 开发部    |
#|      3 | 运维部    |
#+--------+-----------+

for  row  in  session.query(Departments).filter(Departments.dep_id== 2):
  print('#------ %s : %s' %  (row.dep_id, row.dep_name))
#------ 2 : 开发部

for  row  in  session.query(Salary).\
  filter(Salary.award< 5000).filter(Salary.basic>9000):
  print(row.auto_id,row.emp_id,row.date, row.basic, row.award)
#2019-04-25 14:22:51,976 INFO sqlalchemy.engine.base.Engine
# SELECT salary.auto_id AS salary_auto_id, salary.emp_id AS salary_emp_id, salary.date AS salary_date, salary.basic AS salary_basic, salary.award AS salary_award 
#FROM salary 
#WHERE salary.award < %(award_1)s AND salary.basic > %(basic_1)s
#2019-04-25 14:22:51,977 INFO sqlalchemy.engine.base.Engine {'award_1': 5000, 'basic_1': 9000}
#1 1 2019-03-02 10000 2000
#4 2 2019-04-01 10000 3000
#9 5 2019-03-02 9900 2200
#10 5 2019-04-01 9900 3200
#11 6 2019-03-02 11000 2200
#12 6 2019-04-01 11000 2200

for  row  in  session.query(Employees).\
  filter(Employees.emp_name.like('%i%')):
  print('#row.emp_id= %d, row.emp_name= %s, row.gender= %s, row.dep_id= %d'\
  % (row.emp_id, row.emp_name, row.gender, row.dep_id))
#row.emp_id= 2, row.emp_name= alice, row.gender= female, row.dep_id= 1
#row.emp_id= 7, row.emp_name= peri, row.gender= female, row.dep_id= 4

#]# mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy -e "
#> select  *  from   employees where  emp_name like  '%i%';"
#+--------+----------+--------+-------------+--------------+--------+
#| emp_id | emp_name | gender | phone       | email        | dep_id |
#+--------+----------+--------+-------------+--------------+--------+
#|      2 | alice    | female | 15802381238 | alice@qq.com |      1 |
#|      7 | peri     | female | 15802381258 | peri@qq.com  |      4 |

#[root@V0 devops_day02]# mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy -e "
#select  *  from   employees where  emp_name like  'b_b';"
#+--------+----------+--------+-------------+------------+--------+
#| emp_id | emp_name | gender | phone       | email      | dep_id |
#+--------+----------+--------+-------------+------------+--------+
#|      1 | bob      | male   | 13302381238 | bob@qq.com |      1 |
#+--------+----------+--------+-------------+------------+--------+

for  row  in  session.query(Employees).\
  filter(Employees.emp_name.like('b_b')):
  print('#row.emp_id= %d, row.emp_name= %s, row.gender= %s, row.dep_id= %d'\
  % (row.emp_id, row.emp_name, row.gender, row.dep_id))
#row.emp_id= 1, row.emp_name= bob, row.gender= male, row.dep_id= 1

for  row  in  session.query(Employees).\
  filter(Employees.emp_name.in_(['bob', 'alice'])):
  print('#row.emp_id= %d, row.emp_name= %s, row.gender= %s,row.phone= %s, row.dep_id= %d'\
  % (row.emp_id, row.emp_name, row.gender, row.phone, row.dep_id))

#row.emp_id= 1, row.emp_name= bob, row.gender= male,row.phone= 13302381238, row.dep_id= 1
#row.emp_id= 2, row.emp_name= alice, row.gender= female,row.phone= 15802381238, row.dep_id= 1

#]# mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy -e "
#select  *  from   employees where  emp_name in ('bob', 'alice');"
#+--------+----------+--------+-------------+--------------+--------+
#| emp_id | emp_name | gender | phone       | email        | dep_id |
#+--------+----------+--------+-------------+--------------+--------+
#|      1 | bob      | male   | 13302381238 | bob@qq.com   |      1 |
#|      2 | alice    | female | 15802381238 | alice@qq.com |      1 |
#+--------+----------+--------+-------------+--------------+--------+

#]# mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy -e "
#select  *  from   employees where  emp_name  not  in ('bob', 'alice');"
#+--------+----------+--------+-------------+----------------+--------+
#| emp_id | emp_name | gender | phone       | email          | dep_id |
#+--------+----------+--------+-------------+----------------+--------+
#|      3 | 张三     | male   | 15802581238 | zs@qq.com      |      1 |
#|      4 | 李四     | male   | 13305881255 | lisi@qq.com    |      2 |
#|      5 | 王五     | male   | 13302381238 | ww@qq.com      |      2 |
#|      6 | 赵六     | female | 13502381258 | zhaoliu@qq.com |      3 |
#|      7 | peri     | female | 15802381258 | peri@qq.com    |      4 |
#+--------+----------+--------+-------------+----------------+--------+

#注意这里的~Employees.emp_name.in_(中的波浪号'~'代表not
for  row  in  session.query(Employees).\
  filter(~Employees.emp_name.in_(['bob', 'alice'])):
  print('# %d,   %s,  %s, row.phone= %s,  row.dep_id= %d'\
  % (row.emp_id, row.emp_name, row.gender, row.phone, row.dep_id))
# 3,   张三,  male, row.phone= 15802581238,  row.dep_id= 1
# 4,   李四,  male, row.phone= 13305881255,  row.dep_id= 2
# 5,   王五,  male, row.phone= 13302381238,  row.dep_id= 2
# 6,   赵六,  female, row.phone= 13502381258,  row.dep_id= 3
# 7,   peri,  female, row.phone= 15802381258,  row.dep_id= 4


#[root@V0 devops_day02]# mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy -e "
#insert  into  employees   values
#(8, '老八','male', null, null, 4);"

#[root@V0 devops_day02]# mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy -e "
#insert  into  employees   values
#(9, '九妹','female', null, 'sister@qq.com', 4);"
#[root@V0 devops_day02]# mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy -e "
#select  *  from  employees;"
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

#字段为空.is_(None), 字段不为空.isnot(None)

for  row  in  session.query(Employees).\
  filter(Employees.email.isnot(None)).filter(Employees.phone.is_(None)):
  print('# %d,   %s,  %s, row.phone= %s,  row.email= %s, row.dep_id= %d'\
  % (row.emp_id, row.emp_name, row.gender, row.phone, row.email, row.dep_id))

# 9,   九妹,  female, row.phone= None,  row.email= sister@qq.com, row.dep_id= 4

#多重条件and_
for  row  in  session.query(Employees).\
  filter(and_(Employees.email.is_(None), Employees.phone.is_(None))):
  print('# %d,   %s,  %s, row.phone= %s,  row.email= %s, row.dep_id= %d'\
  % (row.emp_id, row.emp_name, row.gender, row.phone, row.email, row.dep_id))

# 8,   老八,  male, row.phone= None,  row.email= None, row.dep_id= 4

#多重条件or_
for  row  in  session.query(Employees).\
  filter(or_(Employees.phone.like('%55'), Employees.email.is_(None))):
  print('# %d,   %s,  %s, row.phone= %s,  row.email= %s, row.dep_id= %d'\
  % (row.emp_id, row.emp_name, row.gender, row.phone, row.email, row.dep_id))

# 4,   李四,  male, row.phone= 13305881255,  row.email= lisi@qq.com, row.dep_id= 2
# 8,   老八,  male, row.phone= None,  row.email= None, row.dep_id= 4

#all()返回列表

result = session.query(Employees.emp_name, Employees.phone).all()
print(type(result),result, sep='\n')
#<class 'list'>
#[('bob', '13302381238'), ('alice', '15802381238'), ('张三', '15802581238'), ('李四', '13305881255'), ('王五', '13302381238'), ('赵六', '13502381258'), ('peri', '15802381258'), ('老八', None), ('九妹', None)]

result2 = session.query(Employees.emp_name, Employees.gender, Employees.phone).filter(Employees.gender.like('fe%'))
print('\n#result2= %s\n' % result2)
#result2= SELECT employees.emp_name AS employees_emp_name, employees.gender AS employees_gender, employees.phone AS employees_phone 
#FROM employees 
#WHERE employees.gender LIKE %(gender_1)s

print(result2.all())
#[('alice', 'female', '15802381238'), ('赵六', 'female', '13502381258'), ('peri', 'female', '15802381258'), ('九妹', 'female', None)]

#first()返回结果中的第一条记录
print(result2.first())
#('alice', 'female', '15802381238')

#one()取出所有记录,如果不是一条记录则抛出异常
#这里查询结果email 是空值的记录只有一条,不报错,返回元组类型的数据
result = session.query(Employees.emp_name, Employees.email).\
         filter(Employees.email.is_(None)).one()
print('\nfilter(Employees.email.is_(None)).one()-----result=', result)
#filter(Employees.email.is_(None)).one()-----result= ('老八', None)


#scalar()调用one(),返回第一列的值
result = session.query(Employees.emp_name, Employees.email).\
         filter(Employees.email.is_(None)).scalar()
print('\nresult= %s\n' % result)
#result= 老八

print('================ ===================== ===============\n')

#通过count()方法,统计行数,聚合函数
print('session.query(Employees).count()= %d\n' % session.query(Employees).count())
#session.query(Employees).count()= 9


#多表查询通过join()方法实现
leftjoin = session.query(Employees.emp_name,Employees.phone,\
           Departments.dep_name).join(Departments,\
           Employees.dep_id == Departments.dep_id)

print('leftjoin = %s\n' % leftjoin)
#leftjoin = SELECT employees.emp_name AS employees_emp_name, employees.phone AS employees_phone, departments.dep_name AS departments_dep_name 
#FROM employees INNER JOIN departments ON employees.dep_id = departments.dep_id

print('leftjoin.all() = %s\n' % leftjoin.all())
#leftjoin.all() = [('bob', '13302381238', '人力部'), ('alice', '15802381238', '人力部'), ('张三', '15802581238', '人力部'), ('李四', '13305881255', '开发部'), ('王五', '13302381238', '开发部'), ('赵六', '13502381258', '运维部'), ('peri', '15802381258', '财务部'), ('老八', None, '财务部'), ('九妹', None, '财务部')]

#[root@V0 devops_day02]# mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy -e "
#> select e.emp_name, e.phone, d.dep_name 
#> from  employees as e
#> left  join  departments as  d
#> on   e.dep_id = d.dep_id;"
#+----------+-------------+-----------+
#| emp_name | phone       | dep_name  |
#+----------+-------------+-----------+
#| bob      | 13302381238 | 人力部    |
#| alice    | 15802381238 | 人力部    |
#| 张三     | 15802581238 | 人力部    |
#| 李四     | 13305881255 | 开发部    |
#| 王五     | 13302381238 | 开发部    |
#| 赵六     | 13502381258 | 运维部    |
#| peri     | 15802381258 | 财务部    |
#| 老八     | NULL        | 财务部    |
#| 九妹     | NULL        | 财务部    |
#+----------+-------------+-----------+

#多表查询通过join()方法实现
leftjoin2 = session.query(Employees.emp_name,Employees.emp_id,\
           Salary.basic+Salary.award).join(\
           Salary, Employees.emp_id == Salary.emp_id)

print('\nleftjoin2.all() = %s\n' % leftjoin2.all())
#leftjoin2.all() = [('bob', 1, 12000), ('bob', 1, 14990), ('alice', 2, 11000), ('alice', 2, 13000), ('张三', 3, 10000), ('张三', 3, 10000), ('李四', 4, 11000), ('李四', 4, 11000), ('王五', 5, 12100), ('王五', 5, 13100), ('赵六', 6, 13200), ('赵六', 6, 13200), ('peri', 7, 18000), ('peri', 7, 18000)]

#[root@V0 devops_day02]# mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy -e "
#> select e.emp_name, e.emp_id, s.basic+s.award as total
#> from  employees as e
#> left  join  salary  as  s
#> on   e.emp_id = s.emp_id;"
#+----------+--------+-------+
#| emp_name | emp_id | total |
#+----------+--------+-------+
#| bob      |      1 | 12000 |
#| bob      |      1 | 14990 |
#| alice    |      2 | 11000 |
#| alice    |      2 | 13000 |
#| 张三     |      3 | 10000 |
#| 张三     |      3 | 10000 |
#| 李四     |      4 | 11000 |
#| 李四     |      4 | 11000 |
#| 王五     |      5 | 12100 |
#| 王五     |      5 | 13100 |
#| 赵六     |      6 | 13200 |
#| 赵六     |      6 | 13200 |
#| peri     |      7 | 18000 |
#| peri     |      7 | 18000 |
#| 老八     |      8 |  NULL |
#| 九妹     |      9 |  NULL |
#+----------+--------+-------+
#[root@V0 devops_day02]# 









if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])








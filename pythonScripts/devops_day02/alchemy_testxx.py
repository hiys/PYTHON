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



sql = 'select * from  departments'
res = session.execute(sql).fetchall()
print(res)





if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])


#[root@V0 devops_day02]# python3  alchemy_testxx.py
#__name__ is alchemy_ORM
#type(enginex) = <class 'sqlalchemy.engine.base.Engine'>,  enginex = Engine(mysql+pymysql://root:***@192.168.1.11/alchemy?charset=utf8)
#
#Base.metadata.create_all = <bound method MetaData.create_all of MetaData(bind=None)>, type(Base.metadata.create_all)= <class 'method'>
#
#Sessionmk = sessionmaker(class_='Session', bind=None, autoflush=True, autocommit=False, expire_on_commit=True),  type(Sessionmk)= <class 'sqlalchemy.orm.session.sessionmaker'>
#
#session = <sqlalchemy.orm.session.Session object at 0x7fd3bb2cc358>,  type(session)= <class 'sqlalchemy.orm.session.Session'>
#
#2019-04-26 16:00:41,057 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'sql_mode'
#2019-04-26 16:00:41,057 INFO sqlalchemy.engine.base.Engine {}
#2019-04-26 16:00:41,058 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
#2019-04-26 16:00:41,058 INFO sqlalchemy.engine.base.Engine {}
#2019-04-26 16:00:41,059 INFO sqlalchemy.engine.base.Engine SELECT DATABASE()
#2019-04-26 16:00:41,059 INFO sqlalchemy.engine.base.Engine {}
#2019-04-26 16:00:41,060 INFO sqlalchemy.engine.base.Engine show collation where `Charset` = 'utf8mb4' and `Collation` = 'utf8mb4_bin'
#2019-04-26 16:00:41,060 INFO sqlalchemy.engine.base.Engine {}
#2019-04-26 16:00:41,061 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS CHAR(60)) AS anon_1
#2019-04-26 16:00:41,061 INFO sqlalchemy.engine.base.Engine {}
#2019-04-26 16:00:41,062 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS CHAR(60)) AS anon_1
#2019-04-26 16:00:41,062 INFO sqlalchemy.engine.base.Engine {}
#2019-04-26 16:00:41,063 INFO sqlalchemy.engine.base.Engine SELECT CAST('test collated returns' AS CHAR CHARACTER SET utf8mb4) COLLATE utf8mb4_bin AS anon_1
#2019-04-26 16:00:41,063 INFO sqlalchemy.engine.base.Engine {}
#2019-04-26 16:00:41,064 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
#2019-04-26 16:00:41,064 INFO sqlalchemy.engine.base.Engine SELECT departments.dep_id AS departments_dep_id, departments.dep_name AS departments_dep_name 
#FROM departments ORDER BY departments.dep_id
#2019-04-26 16:00:41,064 INFO sqlalchemy.engine.base.Engine {}
#<Departments(dep_name= 人力部)>
#1 : 人力部
#<Departments(dep_name= 开发部)>
#2 : 开发部
#<Departments(dep_name= 运维部)>
#3 : 运维部
#<Departments(dep_name= 财务部)>
#4 : 财务部
#2019-04-26 16:00:41,065 INFO sqlalchemy.engine.base.Engine select * from  departments
#2019-04-26 16:00:41,065 INFO sqlalchemy.engine.base.Engine {}
#[(1, '人力部'), (2, '开发部'), (4, '财务部'), (3, '运维部')]
# sys.argv[0]  is alchemy_testxx.py
#
#[root@V0 devops_day02]# 






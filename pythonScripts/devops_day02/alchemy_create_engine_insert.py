#!/usr/bin/env python3
#coding:UTF-8
"""#coding=UTF-8
#mysql -u用户名 -p密码 -h 服务器IP地址 -P 服务器端MySQL端口号  -D 数据库名 -e  相关mysql的sql语句
finance    英 [ˈfaɪnæns]
           n.资金;财政;金融;
ORM即对象关系映射
对象关系映射器（Object Relational Mappers，ORM）
就是在python中设定一个类，
在mysql中定义一个表，
把关系数据库的表结构映射到这个类上
[root@V0 devops_day02]# python3
..............
>>> import  datetime
>>> 
>>> datetime.datetime.now()
datetime.datetime(2019, 4, 24, 18, 35, 45, 117943)
>>>
>>> date = datetime.datetime.da
datetime.datetime.date(  datetime.datetime.day  
>>>
>>> date = datetime.datetime.date(datetime.datetime.now())
>>> date
datetime.date(2019, 4, 24)
>>> 
>>> quit()
[root@V0 devops_day02]# python3
...............
>>> from   datetime  import  datetime
>>> datetime.now()
datetime.datetime(2019, 4, 24, 18, 39, 16, 484021)
>>> date = datetime.da
datetime.date(  datetime.day    
>>> date = datetime.date(datetime.now())
>>> 
>>> date
datetime.date(2019, 4, 24)
>>> type(date)
<class 'datetime.date'>
>>> print(date)
2019-04-24
>>> 
"""
import  sys,  subprocess
from  alchemy_ORM  import  Departments, Employees, Salary, session
from   datetime    import  datetime


sqlcmd = "\'delete  from  salary;\
delete  from  employees;\
delete  from  departments;\'"

mysqlshell= "mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  %s" %  sqlcmd

rcmd = subprocess.call(mysqlshell, shell = True)

if rcmd == 0:
  print('-----delete from well done ---- rcmd  --------\n')
else:
  print('----- rcmd = %d -------\n' % rcmd)


#创建多个实例
#创建映射类Departments(), Employees(), Salary()的实例时,
#并不会真正在表departments, employees, salary中添加记录
dep_hr = Departments(dep_name='人力部')
dep_dev = Departments(dep_name='开发部')
dep_ops = Departments(dep_name='运维部')
dep_finance = Departments(dep_name='财务部')

emp_bob = Employees(
  emp_name='bob',
  gender = 'male',
  phone = '13302381238',
  email = 'bob@qq.com',
  dep_id = 1
)

emp_alice = Employees(
  emp_name='alice',
  gender = 'female',
  phone = '15802381238',
  email = 'alice@qq.com',
  dep_id = 1
)

emp_zs = Employees(
  emp_name='张三',
  gender = 'male',
  phone = '15802581238',
  email = 'zs@qq.com',
  dep_id = 1
)

emp_lisi = Employees(
  emp_name='李四',
  gender = 'male',
  phone = '13305881255',
  email = 'lisi@qq.com',
  dep_id = 2
)

emp_ww = Employees(
  emp_name='王五',
  gender = 'male',
  phone = '13302381238',
  email = 'ww@qq.com',
  dep_id = 2
)

emp_zl = Employees(
  emp_name='赵六',
  gender = 'female',
  phone = '13502381258',
  email = 'zhaoliu@qq.com',
  dep_id = 3
)

emp_peri = Employees(
  emp_name='peri',
  gender = 'female',
  phone = '15802381258',
  email = 'peri@qq.com',
  dep_id = 4
)



##批量添加多个实例的记录
session.add_all([dep_hr, dep_dev, dep_ops, dep_finance])
session.commit()


##添加单个实例的记录
session.add(emp_bob)

##批量添加多个实例的记录
session.add_all([emp_alice, emp_zs, emp_lisi, emp_ww, emp_zl, emp_peri])

session.commit()


date=datetime.date(datetime.now())
print(date,end = '--------------date\n\n')

##创建多个实例
sal_bob_201904 = Salary(
  emp_id = 1,
  date = datetime.date(datetime.now()),
  basic = 9990, 
  award = 5000
)

sal_bob_201903 = Salary(
  emp_id = 1,
  date = '2019-03-02',
  basic = 10000,
  award = 2000
)

sal_alice_201903 = Salary(
  emp_id = 2,
  date = '2019-03-01',
  basic = 9000, 
  award = 2000
)
sal_alice_201904 = Salary(
  emp_id = 2,
  date = '2019-04-01',
  basic = 10000,
  award = 3000
)

sal_zs_201903 = Salary(
  emp_id = 3,
  date = '2019-03-02',
  basic = 8000, 
  award = 2000
)
sal_zs_201904 = Salary(
  emp_id = 3,
  date = '2019-04-02',
  basic = 8000,
  award = 2000
)

sal_lisi_201903 = Salary(
  emp_id = 4,
  date = '2019-03-02',
  basic = 9000,
  award = 2000
)

sal_lisi_201904 = Salary(
  emp_id = 4,
  date = '2019-04-02',
  basic = 9000,
  award = 2000
)

sal_ww_201903 = Salary(
  emp_id = 5,
  date = '2019-03-02',
  basic = 9900,
  award = 2200
)
sal_ww_201904 = Salary(
  emp_id = 5,
  date = '2019-04-01',
  basic = 9900,
  award = 3200
)

sal_zl_201903 = Salary(
  emp_id = 6,
  date = '2019-03-02',
  basic = 11000,
  award = 2200
)
sal_zl_201904 = Salary(
  emp_id = 6,
  date = '2019-04-01',
  basic = 11000,
  award = 2200
)

sal_peri_201903 = Salary(
  emp_id = 7,
  date = '2019-03-02',
  basic = 13000,
  award = 5000
)
sal_peri_201904 = Salary(
  emp_id = 7,
  date = '2019-04-01',
  basic = 13000,
  award = 5000
)


session.add_all([sal_bob_201903, sal_bob_201904,
sal_alice_201903,sal_alice_201904, sal_zs_201903,sal_zs_201904, 
sal_lisi_201903, sal_lisi_201904,  sal_ww_201903,sal_ww_201904,
sal_zl_201903,   sal_zl_201904, sal_peri_201903,sal_peri_201904
])

session.commit()


session.close()
#

sqlcmd = "\'show  tables;\
select  dep_id, dep_name  from  departments;\
select  *  from   employees;\
select  *  from   salary;\'"

mysqlshell= "mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  %s" %  sqlcmd

rcmd2 = subprocess.call(mysqlshell, shell = True)
  
if rcmd2 == 0:
  print('-----OK ---- rcmd2  --------\n')
else:
  print('----- rcmd2 = %d -------\n' % rcmd2)


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])




#[root@V0 devops_day02]# python3  alchemy_create_engine_insert.py__name__ is alchemy_ORM
#type(enginex) = <class 'sqlalchemy.engine.base.Engine'>,  enginex = Engine(mysql+pymysql://root:***@192.168.1.11/alchemy?charset=utf8)
#
#Base.metadata.create_all = <bound method MetaData.create_all of MetaData(bind=None)>, type(Base.metadata.create_all)= <class 'method'>
#
#Sessionmk = sessionmaker(class_='Session', bind=None, autoflush=True, autocommit=False, expire_on_commit=True),  type(Sessionmk)= <class 'sqlalchemy.orm.session.sessionmaker'>
#
#session = <sqlalchemy.orm.session.Session object at 0x7f49241c97b8>,  type(session)= <class 'sqlalchemy.orm.session.Session'>
#
#-----delete from well done ---- rcmd  --------
#
#2019-04-25 10:32:47,505 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'sql_mode'
#2019-04-25 10:32:47,505 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:32:47,506 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
#2019-04-25 10:32:47,506 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:32:47,507 INFO sqlalchemy.engine.base.Engine SELECT DATABASE()
#2019-04-25 10:32:47,507 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:32:47,508 INFO sqlalchemy.engine.base.Engine show collation where `Charset` = 'utf8mb4' and `Collation` = 'utf8mb4_bin'
#2019-04-25 10:32:47,508 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:32:47,509 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS CHAR(60)) AS anon_1
#2019-04-25 10:32:47,509 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:32:47,510 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS CHAR(60)) AS anon_1
#2019-04-25 10:32:47,510 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:32:47,511 INFO sqlalchemy.engine.base.Engine SELECT CAST('test collated returns' AS CHAR CHARACTER SET utf8mb4) COLLATE utf8mb4_bin AS anon_1
#2019-04-25 10:32:47,511 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:32:47,512 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
#2019-04-25 10:32:47,513 INFO sqlalchemy.engine.base.Engine INSERT INTO departments (dep_name) VALUES (%(dep_name)s)
#2019-04-25 10:32:47,513 INFO sqlalchemy.engine.base.Engine {'dep_name': '人力部'}
#2019-04-25 10:32:47,513 INFO sqlalchemy.engine.base.Engine INSERT INTO departments (dep_name) VALUES (%(dep_name)s)
#2019-04-25 10:32:47,513 INFO sqlalchemy.engine.base.Engine {'dep_name': '开发部'}
#2019-04-25 10:32:47,514 INFO sqlalchemy.engine.base.Engine INSERT INTO departments (dep_name) VALUES (%(dep_name)s)
#2019-04-25 10:32:47,514 INFO sqlalchemy.engine.base.Engine {'dep_name': '运维部'}
#2019-04-25 10:32:47,514 INFO sqlalchemy.engine.base.Engine INSERT INTO departments (dep_name) VALUES (%(dep_name)s)
#2019-04-25 10:32:47,514 INFO sqlalchemy.engine.base.Engine {'dep_name': '财务部'}
#2019-04-25 10:32:47,515 INFO sqlalchemy.engine.base.Engine COMMIT
#2019-04-25 10:32:47,559 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
#2019-04-25 10:32:47,560 INFO sqlalchemy.engine.base.Engine INSERT INTO employees (emp_name, gender, phone, email, dep_id) VALUES (%(emp_name)s, %(gender)s, %(phone)s, %(email)s, %(dep_id)s)
#2019-04-25 10:32:47,560 INFO sqlalchemy.engine.base.Engine {'emp_name': 'bob', 'gender': 'male', 'phone': '13302381238', 'email': 'bob@qq.com', 'dep_id': 1}
#2019-04-25 10:32:47,561 INFO sqlalchemy.engine.base.Engine INSERT INTO employees (emp_name, gender, phone, email, dep_id) VALUES (%(emp_name)s, %(gender)s, %(phone)s, %(email)s, %(dep_id)s)
#2019-04-25 10:32:47,561 INFO sqlalchemy.engine.base.Engine {'emp_name': 'alice', 'gender': 'female', 'phone': '15802381238', 'email': 'alice@qq.com', 'dep_id': 1}
#2019-04-25 10:32:47,562 INFO sqlalchemy.engine.base.Engine INSERT INTO employees (emp_name, gender, phone, email, dep_id) VALUES (%(emp_name)s, %(gender)s, %(phone)s, %(email)s, %(dep_id)s)
#2019-04-25 10:32:47,562 INFO sqlalchemy.engine.base.Engine {'emp_name': '张三', 'gender': 'male', 'phone': '15802581238', 'email': 'zs@qq.com', 'dep_id': 1}
#2019-04-25 10:32:47,563 INFO sqlalchemy.engine.base.Engine INSERT INTO employees (emp_name, gender, phone, email, dep_id) VALUES (%(emp_name)s, %(gender)s, %(phone)s, %(email)s, %(dep_id)s)
#2019-04-25 10:32:47,563 INFO sqlalchemy.engine.base.Engine {'emp_name': '李四', 'gender': 'male', 'phone': '13305881255', 'email': 'lisi@qq.com', 'dep_id': 2}
#2019-04-25 10:32:47,564 INFO sqlalchemy.engine.base.Engine INSERT INTO employees (emp_name, gender, phone, email, dep_id) VALUES (%(emp_name)s, %(gender)s, %(phone)s, %(email)s, %(dep_id)s)
#2019-04-25 10:32:47,564 INFO sqlalchemy.engine.base.Engine {'emp_name': '王五', 'gender': 'male', 'phone': '13302381238', 'email': 'ww@qq.com', 'dep_id': 2}
#2019-04-25 10:32:47,564 INFO sqlalchemy.engine.base.Engine INSERT INTO employees (emp_name, gender, phone, email, dep_id) VALUES (%(emp_name)s, %(gender)s, %(phone)s, %(email)s, %(dep_id)s)
#2019-04-25 10:32:47,564 INFO sqlalchemy.engine.base.Engine {'emp_name': '赵六', 'gender': 'female', 'phone': '13502381258', 'email': 'zhaoliu@qq.com', 'dep_id': 3}
#2019-04-25 10:32:47,565 INFO sqlalchemy.engine.base.Engine INSERT INTO employees (emp_name, gender, phone, email, dep_id) VALUES (%(emp_name)s, %(gender)s, %(phone)s, %(email)s, %(dep_id)s)
#2019-04-25 10:32:47,565 INFO sqlalchemy.engine.base.Engine {'emp_name': 'peri', 'gender': 'female', 'phone': '15802381258', 'email': 'peri@qq.com', 'dep_id': 4}
#2019-04-25 10:32:47,566 INFO sqlalchemy.engine.base.Engine COMMIT
#2019-04-25--------------date
#
#2019-04-25 10:32:47,588 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
#2019-04-25 10:32:47,589 INFO sqlalchemy.engine.base.Engine INSERT INTO salary (emp_id, date, basic, award) VALUES (%(emp_id)s, %(date)s, %(basic)s, %(award)s)
#2019-04-25 10:32:47,589 INFO sqlalchemy.engine.base.Engine {'emp_id': 1, 'date': '2019-03-02', 'basic': 10000, 'award': 2000}
#2019-04-25 10:32:47,590 INFO sqlalchemy.engine.base.Engine INSERT INTO salary (emp_id, date, basic, award) VALUES (%(emp_id)s, %(date)s, %(basic)s, %(award)s)
#2019-04-25 10:32:47,590 INFO sqlalchemy.engine.base.Engine {'emp_id': 1, 'date': datetime.date(2019, 4, 25), 'basic': 9990, 'award': 5000}
#2019-04-25 10:32:47,591 INFO sqlalchemy.engine.base.Engine INSERT INTO salary (emp_id, date, basic, award) VALUES (%(emp_id)s, %(date)s, %(basic)s, %(award)s)
#2019-04-25 10:32:47,591 INFO sqlalchemy.engine.base.Engine {'emp_id': 2, 'date': '2019-03-01', 'basic': 9000, 'award': 2000}
#2019-04-25 10:32:47,592 INFO sqlalchemy.engine.base.Engine INSERT INTO salary (emp_id, date, basic, award) VALUES (%(emp_id)s, %(date)s, %(basic)s, %(award)s)
#2019-04-25 10:32:47,592 INFO sqlalchemy.engine.base.Engine {'emp_id': 2, 'date': '2019-04-01', 'basic': 10000, 'award': 3000}
#2019-04-25 10:32:47,592 INFO sqlalchemy.engine.base.Engine INSERT INTO salary (emp_id, date, basic, award) VALUES (%(emp_id)s, %(date)s, %(basic)s, %(award)s)
#2019-04-25 10:32:47,592 INFO sqlalchemy.engine.base.Engine {'emp_id': 3, 'date': '2019-03-02', 'basic': 8000, 'award': 2000}
#2019-04-25 10:32:47,593 INFO sqlalchemy.engine.base.Engine INSERT INTO salary (emp_id, date, basic, award) VALUES (%(emp_id)s, %(date)s, %(basic)s, %(award)s)
#2019-04-25 10:32:47,593 INFO sqlalchemy.engine.base.Engine {'emp_id': 3, 'date': '2019-04-02', 'basic': 8000, 'award': 2000}
#2019-04-25 10:32:47,594 INFO sqlalchemy.engine.base.Engine INSERT INTO salary (emp_id, date, basic, award) VALUES (%(emp_id)s, %(date)s, %(basic)s, %(award)s)
#2019-04-25 10:32:47,594 INFO sqlalchemy.engine.base.Engine {'emp_id': 4, 'date': '2019-03-02', 'basic': 9000, 'award': 2000}
#2019-04-25 10:32:47,595 INFO sqlalchemy.engine.base.Engine INSERT INTO salary (emp_id, date, basic, award) VALUES (%(emp_id)s, %(date)s, %(basic)s, %(award)s)
#2019-04-25 10:32:47,595 INFO sqlalchemy.engine.base.Engine {'emp_id': 4, 'date': '2019-04-02', 'basic': 9000, 'award': 2000}
#2019-04-25 10:32:47,595 INFO sqlalchemy.engine.base.Engine INSERT INTO salary (emp_id, date, basic, award) VALUES (%(emp_id)s, %(date)s, %(basic)s, %(award)s)
#2019-04-25 10:32:47,595 INFO sqlalchemy.engine.base.Engine {'emp_id': 5, 'date': '2019-03-02', 'basic': 9900, 'award': 2200}
#2019-04-25 10:32:47,596 INFO sqlalchemy.engine.base.Engine INSERT INTO salary (emp_id, date, basic, award) VALUES (%(emp_id)s, %(date)s, %(basic)s, %(award)s)
#2019-04-25 10:32:47,596 INFO sqlalchemy.engine.base.Engine {'emp_id': 5, 'date': '2019-04-01', 'basic': 9900, 'award': 3200}
#2019-04-25 10:32:47,597 INFO sqlalchemy.engine.base.Engine INSERT INTO salary (emp_id, date, basic, award) VALUES (%(emp_id)s, %(date)s, %(basic)s, %(award)s)
#2019-04-25 10:32:47,597 INFO sqlalchemy.engine.base.Engine {'emp_id': 6, 'date': '2019-03-02', 'basic': 11000, 'award': 2200}
#2019-04-25 10:32:47,598 INFO sqlalchemy.engine.base.Engine INSERT INTO salary (emp_id, date, basic, award) VALUES (%(emp_id)s, %(date)s, %(basic)s, %(award)s)
#2019-04-25 10:32:47,598 INFO sqlalchemy.engine.base.Engine {'emp_id': 6, 'date': '2019-04-01', 'basic': 11000, 'award': 2200}
#2019-04-25 10:32:47,598 INFO sqlalchemy.engine.base.Engine INSERT INTO salary (emp_id, date, basic, award) VALUES (%(emp_id)s, %(date)s, %(basic)s, %(award)s)
#2019-04-25 10:32:47,599 INFO sqlalchemy.engine.base.Engine {'emp_id': 7, 'date': '2019-03-02', 'basic': 13000, 'award': 5000}
#2019-04-25 10:32:47,599 INFO sqlalchemy.engine.base.Engine INSERT INTO salary (emp_id, date, basic, award) VALUES (%(emp_id)s, %(date)s, %(basic)s, %(award)s)
#2019-04-25 10:32:47,599 INFO sqlalchemy.engine.base.Engine {'emp_id': 7, 'date': '2019-04-01', 'basic': 13000, 'award': 5000}
#2019-04-25 10:32:47,600 INFO sqlalchemy.engine.base.Engine COMMIT
#+-------------------+
#| Tables_in_alchemy |
#+-------------------+
#| departments       |
#| employees         |
#| salary            |
#+-------------------+
#+--------+-----------+
#| dep_id | dep_name  |
#+--------+-----------+
#|      1 | 人力部    |
#|      2 | 开发部    |
#|      4 | 财务部    |
#|      3 | 运维部    |
#+--------+-----------+
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
#+--------+----------+--------+-------------+----------------+--------+
#+---------+--------+------------+-------+-------+
#| auto_id | emp_id | date       | basic | award |
#+---------+--------+------------+-------+-------+
#|       1 |      1 | 2019-03-02 | 10000 |  2000 |
#|       2 |      1 | 2019-04-25 |  9990 |  5000 |
#|       3 |      2 | 2019-03-01 |  9000 |  2000 |
#|       4 |      2 | 2019-04-01 | 10000 |  3000 |
#|       5 |      3 | 2019-03-02 |  8000 |  2000 |
#|       6 |      3 | 2019-04-02 |  8000 |  2000 |
#|       7 |      4 | 2019-03-02 |  9000 |  2000 |
#|       8 |      4 | 2019-04-02 |  9000 |  2000 |
#|       9 |      5 | 2019-03-02 |  9900 |  2200 |
#|      10 |      5 | 2019-04-01 |  9900 |  3200 |
#|      11 |      6 | 2019-03-02 | 11000 |  2200 |
#|      12 |      6 | 2019-04-01 | 11000 |  2200 |
#|      13 |      7 | 2019-03-02 | 13000 |  5000 |
#|      14 |      7 | 2019-04-01 | 13000 |  5000 |
#+---------+--------+------------+-------+-------+
#-----OK ---- rcmd2  --------
#
# sys.argv[0]  is alchemy_create_engine_insert.py
#
#[root@V0 devops_day02]# 




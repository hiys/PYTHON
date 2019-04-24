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
  print('-----OK ---- rcmd  --------\n')
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

sal_bob_201804 = Salary(
  emp_id = 1,
  date = '2018-04-02',
  basic = 10000,
  award = 2000
)

sal_alice_201803 = Salary(
  emp_id = 2,
  date = '2018-03-01',
  basic = 10000, 
  award = 5000
)
sal_alice_201804 = Salary(
  emp_id = 2,
  date = '2018-04-01',
  basic = 10000,
  award = 5000
)

sal_zs_201803 = Salary(
  emp_id = 3,
  date = '2018-03-01',
  basic = 8000, 
  award = 2000
)

session.add(sal_bob_201803)

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








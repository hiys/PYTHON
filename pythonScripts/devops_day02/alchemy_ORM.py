#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
#mysql -u用户名 -p密码 -h 服务器IP地址 -P 服务器端MySQL端口号  -D 数据库名 -e  相关mysql的sql语句
CMD	Command	命令
ORM即对象关系映射
对象关系映射器（Object Relational Mappers，ORM）
就是在python中设定一个类，
在mysql中定义一个表，
把关系数据库的表结构映射到这个类上

relative      美 [ˈrelətɪv]  
      adj.相比较而言的;比较的;相对的;
absolute      英 [ˈæbsəluːt] 
      adj.完全的;全部的;绝对的;
alchemy       美 [ˈælkəmi]  
       n.炼金术, 神秘力量，魔力
oracle        美 [ˈɔːrəkl]  
       n. 权威;智囊
declarative    英 [dɪˈklærətɪv]
      adj.陈述的
schema         英 [ˈskiːmə]
   n.(计划或理论的)提要，纲要
session        英 [ˈseʃn]
   n.一场;一节;一段时间;(法庭的)开庭，开庭期;(议会等的)会议，会期;

# cat   ~/.pip/pip.conf  #使用国内镜像站点,注意在root的家目录下有效
[global]
index-url = http://pypi.doubanio.com/simple/
[install]
trusted-host = pypi.doubanio.com

# pip3    install    pymysql    #下载安装 pymysql 模块
# pip3    install   sqlalchemy

#Table 构造方法
#Table(name, metadata[, *column_list][, **kwargs])
#参数说明:
#name 表名
#metadata 元数据对象
#column_list 是列(Column或其他继承自SchemaItem的对象)列表
#kwargs主要内容：
#
#schema: (None)表的模式（一般默认是数据库名, 无需特别指定; 
#Oracle中是owner, 当一个数据库由多个用户管理时，
#用户的默认数据库不是要连接的数据库时，需要指定此项）
#
#Column构造函数相关设置
#name：字段名
#type_ 字段数据类型，
#这里的数据类型包括：
#SQLAlchemy中常用数据类型:
#整数: SmallInteger、Integer、BigInteger等
#浮点数: Float、Numeric等
#文本字符串: String、Text、Unicode、UnicodeText、CHAR、VARCHAR等
#二进制字符串: LargeBinary、BINARY、VARBINARY等
#日期时间: Date、DateTime、TIMESTAMP等
#
#Constraint: 约束
#ForeignKey: 外键
#ColumnDefault: 列默认值
#kwargs主要内容：
#autoincrement: (False)是否数字自动增加1
#default: (None)默认值
#index: (None)索引
#nullable: (True)是否可以为空(NULL)
#primary_key: (False)是否是主键
#server_default: (None)服务端(数据库中的函数)默认值
#unique: (False)是否唯一
#comment: (None)列注释

#创建映射类Departments(Base),创建架构
#映射类构建完成后,表的信息将被写入到表的元数据(metadata)
#Table 构造方法
#Table(name, metadata[, *column_list][, **kwargs])
"""

import  sys,  subprocess

from   sqlalchemy  import  create_engine, Column, Integer, String,  ForeignKey, Date
from   sqlalchemy.ext.declarative  import  declarative_base
from   sqlalchemy.orm  import  sessionmaker

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

#通过create_engine实现数据库的连接
#create_engine('使用的数据库类型(比如mysql,oracle等) + python的pymysql模块://用户名:用户的密码@连接的数据库服务器主机/主机上的数据库名?charset=utf8',encoding='utf8', echo=True)
#echo=True表示将日志输出到终端屏幕,默认为False
#  "mysql+pymysql://root:123@/alchemy",#这里@后面不写连接的数据库服务器主机
#  表示默认数据库服务器主机是本机

enginex = create_engine(
  #  在连接数据库的时候声明引擎编码方式'utf8'
  'mysql+pymysql://root:123@192.168.1.11/alchemy?charset=utf8',#这里不能有空格
  encoding = 'utf-8', #这里可以有空格,设置本地的编码方式为utf-8
  echo = True
)

print('type(enginex) = %s,  enginex = %s\n' % (type(enginex), enginex))


#首先通过声明系统,定义基类Base, 使用声明层作为基类
Base = declarative_base() #创建映射类的基本类

print('Base.metadata.create_all = %s, type(Base.metadata.create_all)= %s\n' \
      %  (Base.metadata.create_all, type(Base.metadata.create_all)))


###以下三行是创建句柄类的另一种 方式
#Session = sessionmaker(enginex)
#session = Session()
#session.add_all([dep_hr, dep_ops, dep_dev])#批量添加记录

#ORM即对象关系映射
#创建句柄类Sessionmk(名称自定义)
#ORM访问数据库的句柄被称作Session
Sessionmk = sessionmaker()

print('Sessionmk = %s,  type(Sessionmk)= %s' %  (Sessionmk, type(Sessionmk)))

#绑定引擎enginex,创建会话类实例对象session
#会话类的实例对象session用于绑定到数据库
session = Sessionmk(bind= enginex)

print('\nsession = %s,  type(session)= %s\n' %  (session, type(session)))

#Table(name, metadata[, *column_list][, **kwargs])
class  Departments(Base):  #继承基本类Base

  #在alchemy数据库中创建的表名'departments'
  #对__tablename__进行赋值，确定表名
  __tablename__ = 'departments'   #库中的表名
  __table_args__ = { "mysql_charset" : "utf8" } #设置数据库表编码方式为utf8

  #Integer整数类型, autoincrement数字自动增加1,primary_key主键
  dep_id = Column(Integer, autoincrement= True, primary_key= True)

  # String字符串类型，nullable非空约束，unique唯一性约束
  dep_name = Column(String(20), nullable= False, unique= True)

  def  __str__(self):  #打印/显示实例时调用内建方法str
    return  '<Departments(dep_name= %s)>'  %  self.dep_name


class  Employees(Base):
  __tablename__ = 'employees'
  emp_id = Column(Integer, autoincrement= True, primary_key= True)
  emp_name = Column(String(20), nullable = False)
  gender = Column(String(10))
  phone = Column(String(11))
  email = Column(String(50))
  dep_id = Column(Integer, ForeignKey('departments.dep_id'))

  def  __str__(self):  #打印/显示实例时调用内建方法str
    return  '<Employees(emp_name= %s)>' % self.emp_name


class  Salary(Base):
  __tablename__ = 'salary'
  auto_id = Column(Integer, autoincrement=True, primary_key= True)
  emp_id = Column(Integer, ForeignKey('employees.emp_id'))
  date = Column(Date)
  basic = Column(Integer)
  award = Column(Integer)




if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])


  mysqlshell= 'mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy \
    -e "drop table salary;drop table  employees; drop  table  departments;"'
  returncmd = subprocess.call(mysqlshell, shell = True)
  #无法返回命令的输出,只会返回函数运行成功与否的0或其他值。
  if returncmd == 0:
    print('-----------OK----------------\n')
  else:
    print('-----returncmd = %d -------\n' % returncmd)
  
  
  #通过表的映射类Departments(Base), Employees(Base),在数据库中创建表,
  #enginex是自定义引擎<class 'sqlalchemy.engine.base.Engine'>
  #映射类构建完成后,表的信息将被写入到表的元数据(metadata)
  
  Base.metadata.create_all(enginex)
  
  

#[root@V0 devops_day02]# python3  alchemy_ORM.py
#__name__ is __main__
#type(enginex) = <class 'sqlalchemy.engine.base.Engine'>,  enginex = Engine(mysql+pymysql://root:***@192.168.1.11/alchemy?charset=utf8)
#
#Base.metadata.create_all = <bound method MetaData.create_all of MetaData(bind=None)>, type(Base.metadata.create_all)= <class 'method'>
#
#Sessionmk = sessionmaker(class_='Session', bind=None, autoflush=True, autocommit=False, expire_on_commit=True),  type(Sessionmk)= <class 'sqlalchemy.orm.session.sessionmaker'>
#
#session = <sqlalchemy.orm.session.Session object at 0x7ff698fb6208>,  type(session)= <class 'sqlalchemy.orm.session.Session'>
#
# sys.argv[0]  is alchemy_ORM.py
#
#-----------OK----------------
#
#2019-04-25 10:28:37,232 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'sql_mode'
#2019-04-25 10:28:37,232 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:28:37,236 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
#2019-04-25 10:28:37,236 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:28:37,240 INFO sqlalchemy.engine.base.Engine SELECT DATABASE()
#2019-04-25 10:28:37,240 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:28:37,243 INFO sqlalchemy.engine.base.Engine show collation where `Charset` = 'utf8mb4' and `Collation` = 'utf8mb4_bin'
#2019-04-25 10:28:37,243 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:28:37,248 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS CHAR(60)) AS anon_1
#2019-04-25 10:28:37,248 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:28:37,250 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS CHAR(60)) AS anon_1
#2019-04-25 10:28:37,251 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:28:37,253 INFO sqlalchemy.engine.base.Engine SELECT CAST('test collated returns' AS CHAR CHARACTER SET utf8mb4) COLLATE utf8mb4_bin AS anon_1
#2019-04-25 10:28:37,253 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:28:37,256 INFO sqlalchemy.engine.base.Engine DESCRIBE `departments`
#2019-04-25 10:28:37,257 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:28:37,258 INFO sqlalchemy.engine.base.Engine ROLLBACK
#2019-04-25 10:28:37,259 INFO sqlalchemy.engine.base.Engine DESCRIBE `employees`
#2019-04-25 10:28:37,260 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:28:37,261 INFO sqlalchemy.engine.base.Engine ROLLBACK
#2019-04-25 10:28:37,261 INFO sqlalchemy.engine.base.Engine DESCRIBE `salary`
#2019-04-25 10:28:37,261 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:28:37,262 INFO sqlalchemy.engine.base.Engine ROLLBACK
#2019-04-25 10:28:37,264 INFO sqlalchemy.engine.base.Engine 
#CREATE TABLE departments (
#	dep_id INTEGER NOT NULL AUTO_INCREMENT, 
#	dep_name VARCHAR(20) NOT NULL, 
#	PRIMARY KEY (dep_id), 
#	UNIQUE (dep_name)
#)CHARSET=utf8
#
#
#2019-04-25 10:28:37,264 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:28:37,303 INFO sqlalchemy.engine.base.Engine COMMIT
#2019-04-25 10:28:37,305 INFO sqlalchemy.engine.base.Engine 
#CREATE TABLE employees (
#	emp_id INTEGER NOT NULL AUTO_INCREMENT, 
#	emp_name VARCHAR(20) NOT NULL, 
#	gender VARCHAR(10), 
#	phone VARCHAR(11), 
#	email VARCHAR(50), 
#	dep_id INTEGER, 
#	PRIMARY KEY (emp_id), 
#	FOREIGN KEY(dep_id) REFERENCES departments (dep_id)
#)
#
#
#2019-04-25 10:28:37,305 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:28:37,345 INFO sqlalchemy.engine.base.Engine COMMIT
#2019-04-25 10:28:37,347 INFO sqlalchemy.engine.base.Engine 
#CREATE TABLE salary (
#	auto_id INTEGER NOT NULL AUTO_INCREMENT, 
#	emp_id INTEGER, 
#	date DATE, 
#	basic INTEGER, 
#	award INTEGER, 
#	PRIMARY KEY (auto_id), 
#	FOREIGN KEY(emp_id) REFERENCES employees (emp_id)
#)
#
#
#2019-04-25 10:28:37,348 INFO sqlalchemy.engine.base.Engine {}
#2019-04-25 10:28:37,378 INFO sqlalchemy.engine.base.Engine COMMIT
#[root@V0 devops_day02]# 







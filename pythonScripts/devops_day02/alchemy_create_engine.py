#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
#mysql -u用户名 -p密码 -h 服务器IP地址 -P 服务器端MySQL端口号  -D 数据库名 -e  相关mysql的sql语句
#[root@V0 ~]# mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy -e "
> select  database();"
+------------+
| database() |
+------------+
| alchemy    |
+------------+

relative      美 [ˈrelətɪv]  
      adj.相比较而言的;比较的;相对的;
absolute      英 [ˈæbsəluːt] 
      adj.完全的;全部的;绝对的;
alchemy       美 [ˈælkəmi]  
       n.炼金术, 神秘力量，魔力
oracle     美 [ˈɔːrəkl]  
       n. 权威;智囊
declarative   英 [dɪˈklærətɪv]
      adj.陈述的
schema      英 [ˈskiːmə]
   n.(计划或理论的)提要，纲要

# cat   ~/.pip/pip.conf  #使用国内镜像站点,注意在root的家目录下有效
[global]
index-url = http://pypi.doubanio.com/simple/
[install]
trusted-host = pypi.doubanio.com

# pip3    install    pymysql    #下载安装 pymysql 模块
# pip3    install   sqlalchemy
"""

import  sys, pymysql

from   sqlalchemy  import  create_engine, Column, Integer, String
from   sqlalchemy.ext.declarative  import  declarative_base


sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

##创建连接conn,访问数据库pysql
#conn =  pymysql.connect(
#  host = '192.168.0.10', #具体的ip地址不允许空密码匿名用户存在
##  host = '127.0.0.10',   #127.0.0.10允许空密码匿名用户存在
#  port = 3306,
#  user = 'root',
#  passwd = '123',
#  db = 'pysql',
#  charset = 'utf8'
#)
#cursor  = conn.cursor()  #创建游标
#
##对数据库表做修改操作,必须要commit提交
#return_commit = conn.commit()
#cursor.close()    #关闭游标
#conn.close()      #关闭数据库pysql 连接


#create_engine('使用的数据库类型(比如mysql,oracle等) + python的pymysql模块://用户名:用户的密码@连接的数据库服务器主机/主机上的数据库名',encoding='utf8', echo=True)
#echo=True表示将日志输出到终端屏幕,默认为False

#  'mysql + pymysql://root:123@192.168.1.11/alchemy','单引号'改为"双引号"
# 注意字符串'mysql + pymysql:....'中有空格会报错
#sqlalchemy.exc.ArgumentError: Could not parse rfc1738 URL from string 'mysql + pymysql://root:123@localhost/alchemy'

#  "mysql+pymysql://root:123@/alchemy",#这里@后面不写连接的数据库服务器主机
#  表示默认数据库服务器主机是本机

enginex = create_engine(
  #  在连接数据库的时候声明编码'utf8'
  'mysql+pymysql://root:123@192.168.1.11/alchemy?charset=utf8',#这里不能有空格
  encoding = 'utf-8', #这里可以有空格,设置引擎编码方式为utf-8
  echo = True
)

print('type(enginex) = %s,  enginex = %s\n' % (type(enginex), enginex))
#type(enginex) = <class 'sqlalchemy.engine.base.Engine'>,  enginex = Engine(mysql+pymysql://root:***@192.168.1.11/alchemy?charset=utf8)


#首先通过声明系统,定义基类Base, 使用声明层作为基类
Base = declarative_base() #创建映射类的基本类

print('Base.metadata.create_all = %s, type(Base.metadata.create_all)= %s\n' \
      %  (Base.metadata.create_all, type(Base.metadata.create_all)))
#Base.metadata.create_all = <bound method MetaData.create_all of MetaData(bind=None)>, type(Base.metadata.create_all)= <class 'method'>


class  Departments(Base):  #继承基本类Base

  #在alchemy数据库中创建的表名'departments'
  #对__tablename__进行赋值，确定表名
  __tablename__ = 'departments'
  __table_args__ = { "mysql_charset" : "utf8" } #设置数据库表编码方式为utf8

  dep_id = Column(Integer, primary_key= True)
  dep_name = Column(String(20), unique= True)

  def  __str__(self):  #打印/显示实例时调用内建方法str
    return  '<Departments(dep_name= %s)>'  %  self.dep_name

print('Departments.__table__ = %s,   type(Departments.__table__) = %s \n' % \
   (Departments.__table__, type(Departments.__table__)))
#Departments.__table__ = departments,   type(Departments.__table__) = <class 'sqlalchemy.sql.schema.Table'>

print('Departments.__table_args__= %s,   type(Departments.__table_args__) = %s \n' % \
    (Departments.__table_args__, type(Departments.__table_args__)))
#Departments.__table_args__= {'mysql_charset': 'utf8'},   type(Departments.__table_args__) = <class 'dict'>


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])

  Base.metadata.create_all(enginex)


#[root@V0 devops_day02]# vim   alchemy_create_engine.py 
#[root@V0 devops_day02]# mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy -e "show tables;"
#[root@V0 devops_day02]# python3   alchemy_create_engine.py
#__name__ is __main__
#type(enginex) = <class 'sqlalchemy.engine.base.Engine'>,  enginex = Engine(mysql+pymysql://root:***@192.168.1.11/alchemy?charset=utf8)
#
#Base.metadata.create_all = <bound method MetaData.create_all of MetaData(bind=None)>, type(Base.metadata.create_all)= <class 'method'>
#
#Departments.__table__ = departments,   type(Departments.__table__) = <class 'sqlalchemy.sql.schema.Table'> 
#
#Departments.__table_args__= {'mysql_charset': 'utf8'},   type(Departments.__table_args__) = <class 'dict'> 
#
# sys.argv[0]  is alchemy_create_engine.py
#
#2019-04-24 11:01:57,389 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'sql_mode'
#2019-04-24 11:01:57,389 INFO sqlalchemy.engine.base.Engine {}
#2019-04-24 11:01:57,390 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
#2019-04-24 11:01:57,390 INFO sqlalchemy.engine.base.Engine {}
#2019-04-24 11:01:57,391 INFO sqlalchemy.engine.base.Engine SELECT DATABASE()
#2019-04-24 11:01:57,391 INFO sqlalchemy.engine.base.Engine {}
#2019-04-24 11:01:57,392 INFO sqlalchemy.engine.base.Engine show collation where `Charset` = 'utf8mb4' and `Collation` = 'utf8mb4_bin'
#2019-04-24 11:01:57,392 INFO sqlalchemy.engine.base.Engine {}
#2019-04-24 11:01:57,393 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS CHAR(60)) AS anon_1
#2019-04-24 11:01:57,393 INFO sqlalchemy.engine.base.Engine {}
#2019-04-24 11:01:57,394 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS CHAR(60)) AS anon_1
#2019-04-24 11:01:57,394 INFO sqlalchemy.engine.base.Engine {}
#2019-04-24 11:01:57,394 INFO sqlalchemy.engine.base.Engine SELECT CAST('test collated returns' AS CHAR CHARACTER SET utf8mb4) COLLATE utf8mb4_bin AS anon_1
#2019-04-24 11:01:57,394 INFO sqlalchemy.engine.base.Engine {}
#2019-04-24 11:01:57,395 INFO sqlalchemy.engine.base.Engine DESCRIBE `departments`
#2019-04-24 11:01:57,395 INFO sqlalchemy.engine.base.Engine {}
#2019-04-24 11:01:57,396 INFO sqlalchemy.engine.base.Engine ROLLBACK
#2019-04-24 11:01:57,396 INFO sqlalchemy.engine.base.Engine 
#CREATE TABLE departments (
#	dep_id INTEGER NOT NULL AUTO_INCREMENT, 
#	dep_name VARCHAR(20), 
#	PRIMARY KEY (dep_id), 
#	UNIQUE (dep_name)
#)CHARSET=utf8
#
#
#2019-04-24 11:01:57,396 INFO sqlalchemy.engine.base.Engine {}
#2019-04-24 11:01:57,467 INFO sqlalchemy.engine.base.Engine COMMIT
#[root@V0 devops_day02]# mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy -e "show tables;"
#+-------------------+
#| Tables_in_alchemy |
#+-------------------+
#| departments       |
#+-------------------+
#[root@V0 devops_day02]# 




#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
"""
import  sys, pymysql
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

#创建连接conn,访问'192.168.0.11'数据库pysql
conn =  pymysql.connect(
  host = '192.168.0.11', #具体的ip地址不允许空密码匿名用户存在
#  host = '127.0.0.10',   #127.0.0.10允许空密码匿名用户存在
  port = 3306,
  user = 'root',
  passwd = '123',
  db = 'pysql',
  charset = 'utf8'
)

#创建连接conn,访问'192.168.1.12'数据库pysql
conn2 =  pymysql.connect(
  host = '192.168.1.12', #具体的ip地址不允许空密码匿名用户存在
  port = 3306,
  user = 'root',
  passwd = '123',
  db = 'pysql',
  charset = 'utf8'
)

cursor  = conn.cursor()  #创建游标
cursor2  = conn2.cursor()  #创建游标

sql_insert1 = "insert into departments values (%s, %s)"

result = cursor.execute(sql_insert1, (7, '行政部'))
print('type(result) = %s ------ result = %s' % (type(result), result))
#对数据库表做修改操作,必须要commit提交
conn.commit()


result2 = cursor2.execute(sql_insert1, (7, '行政部'))
print('type(result2) = %s ---cursor2--- result2 = %s' % (type(result2), result2))
#对数据库表做修改操作,必须要commit提交
conn2.commit()


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])

#==============================
#[root@V0 devops_day02]# python3  pymysqlcursor.py
#__name__ is __main__
#type(result) = <class 'int'> ------ result = 1
#type(result2) = <class 'int'> ---cursor2--- result2 = 1
# sys.argv[0]  is pymysqlcursor.py
#
#[root@V1 pyscripts]# mysql  -uroot -p123  -e  "use pysql;select *  from  departments;"
#+--------+-----------+
#| dep_id | dep_name  |
#+--------+-----------+
#|      1 | 人事部    |
#|      5 | 市场部    |
#|      2 | 开发部    |
#|      4 | 财务部    |
#|      3 | 运维部    |
#|      6 | 销售部    |
#+--------+-----------+
#
#[root@V1 pyscripts]# mysql  -uroot -p123  -e  "use pysql;select *  from  departments;"  |grep  7
#7	行政部
#
#[root@V2 pyscripts]# mysql  -uroot -p123  -e  "use pysql;select *  from  departments;"  |grep  7
#7	行政部





#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
relative     美 [ˈrelətɪv]  
      adj.相比较而言的;比较的;相对的;
absolute     英 [ˈæbsəluːt] 
      adj.完全的;全部的;绝对的;
"""
import  sys, pymysql
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

#创建连接conn,访问数据库pysql
conn =  pymysql.connect(
  host = '192.168.0.10', #具体的ip地址不允许空密码匿名用户存在
#  host = '127.0.0.10',   #127.0.0.10允许空密码匿名用户存在
  port = 3306,
  user = 'root',
  passwd = '123',
  db = 'pysql',
  charset = 'utf8'
)
#print('type(conn) = %s , conn = %s ' % (type(conn), conn))
#type(conn) = <class 'pymysql.connections.Connection'> , conn = <pymysql.connections.Connection object at 0x7f5cea1358d0> 

cursor  = conn.cursor()  #创建游标

#print('type(cursor) = %s , cursor = %s ' % (type(cursor), cursor))
#type(cursor) = <class 'pymysql.cursors.Cursor'> , cursor = <pymysql.cursors.Cursor object at 0x7f5cdf374588> 

#通过update修改某一字段的值
sql_update = "update  departments set dep_name = 'finance' \
              where dep_name = '财务部';"
#result = cursor.execute(sql_update)

#print('type(result) = %s ------ result = %d' % (type(result), result))
#type(result) = <class 'int'> ------ result = 1

#通过delete删除记录
sql_del= "DELETE  from departments where dep_name='finance' and dep_id= %s"

return_data = cursor.execute(sql_del,(4,))

print('type(return_data) = %s ------ return_data = %d' % \
      (type(return_data), return_data))
#type(return_data) = <class 'int'> ------ return_data = 1





#对数据库表做修改操作,必须要commit提交
return_commit = conn.commit()

#print('type(return_commit)= %s ---return_commit = %s' \
#  % (type(return_commit), return_commit))
#type(return_commit)= <class 'NoneType'> ---return_commit = None

cursor.close()    #关闭游标
conn.close()      #关闭数据库pysql 连接

#print(cursor , conn)
#<pymysql.cursors.Cursor object at 0x7f5cdf374588> <pymysql.connections.Connection object at 0x7f5cea1358d0>


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])


#[root@V0 devops_day02]# mysql  -uroot -p123  -e  "use pysql;select *  from  departments;"
#+--------+-----------------+
#| dep_id | dep_name        |
#+--------+-----------------+
#|      1 | 人事部          |
#|      2 | 人力资源部      |
#|      5 | 市场部          |
#|      7 | 行政部          |
#|      4 | 财务部          |
#|      3 | 运维部          |
#|      6 | 销售部          |
#+--------+-----------------+
#[root@V0 devops_day02]# python3    pymysqlupdate.py 
#__name__ is __main__
#type(result) = <class 'int'> ------ result = 1
# sys.argv[0]  is pymysqlupdate.py
#
#[root@V0 devops_day02]# 
#[root@V0 devops_day02]# mysql  -uroot -p123  -e  "use pysql;select *  from  departments;"
#+--------+-----------------+
#| dep_id | dep_name        |
#+--------+-----------------+
#|      4 | finance         |
#|      1 | 人事部          |
#|      2 | 人力资源部      |
#|      5 | 市场部          |
#|      7 | 行政部          |
#|      3 | 运维部          |
#|      6 | 销售部          |
#+--------+-----------------+
#[root@V0 devops_day02]# 

#[root@V0 devops_day02]# python3    pymysqlupdate.py 
#__name__ is __main__
#type(return_data) = <class 'int'> ------ return_data = 1
# sys.argv[0]  is pymysqlupdate.py
#
#[root@V0 devops_day02]# mysql  -uroot -p123  -e  "use pysql;select *  from  departments;"
#+--------+-----------------+
#| dep_id | dep_name        |
#+--------+-----------------+
#|      1 | 人事部          |
#|      2 | 人力资源部      |
#|      5 | 市场部          |
#|      7 | 行政部          |
#|      3 | 运维部          |
#|      6 | 销售部          |
#+--------+-----------------+



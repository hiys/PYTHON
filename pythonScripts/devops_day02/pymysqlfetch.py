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

print('type(conn) = %s , conn = %s ' % (type(conn), conn))
#type(conn) = <class 'pymysql.connections.Connection'> , conn = <pymysql.connections.Connection object at 0x7f5cea1358d0> 

cursor  = conn.cursor()  #创建游标

print('type(cursor) = %s , cursor = %s ' % (type(cursor), cursor))
#type(cursor) = <class 'pymysql.cursors.Cursor'> , cursor = <pymysql.cursors.Cursor object at 0x7f5cdf374588> 

#插入数据
#sql_insert1 = "insert into departments values (%s, %s)" #注意只能是字符串类型%s,不是数字%d
#------------------cursor.execute() ----- 只执行一条语句---
#result = cursor.execute(sql_insert1, (7, '行政部'))

#注意values (%s, %s, %s, %s, %s, %s, %s)" 只能是字符串类型%s,不是数字%d
#sql_insert2 = "insert into employees   values (%s, %s, %s, %s, %s, %s, %s)"
#employees = [
#  (4, 'bob', 'male', '1990-06-09', '13802381238', 'bob@qq.com', 2),
#  (5, 'alice', 'female', '1995-08-08', '15851285125', 'alice@qq.com', 3)
#]
#注意变量 employees 是个列表类型
#-----------cursor.executemany() ----- 执行多条语句---
#result2 = cursor.executemany(sql_insert2, employees)

#查询数据
sql_select = 'select dep_id, dep_name  from  departments order by dep_id;'

return_value = cursor.execute(sql_select)

print('type(return_value)= %s ---return_value = %d' \
  % (type(return_value), return_value))
#type(return_value)= <class 'int'> ---return_value = 7

result1 = cursor.fetchone()  #只查询一条记录
print('type(result1) = %s ------ result1 = %s' % (type(result1), result1))
#type(result1) = <class 'tuple'> ------ result1 = (1, '人事部')

result2 = cursor.fetchmany()  #可以查询多条记录,不写数字,默认只查询一条记录
print('type(result2) = %s ------ result2 = %s' % (type(result2), result2))
#type(result2) = <class 'tuple'> ------ result2 = ((2, '人力资源部'),)

result22 = cursor.fetchmany(2)  #写数字2表示可以查询2条记录并且返回记录
print('type(result22) = %s ------ result22 = %s' % (type(result22), result22))
#type(result22) = <class 'tuple'> ------ result22 = ((3, '运维部'), (4, '财务部'))

result3 = cursor.fetchall()    #可以查询所有剩余的记录
print('type(result3) = %s ------ result3 = %s' % (type(result3), result3))
#type(result3) = <class 'tuple'> ------ result3 = ((5, '市场部'), (6, '销售部'), (7, '行政部'))

#移动游标(2, mode= 'absolute')以绝对的路径从数据库记录的开头往后移动2行记录
return_scroll = cursor.scroll(2, mode= 'absolute')
print('type(return_scroll)= %s ---- return_scroll= %s' % (type(return_scroll), return_scroll))
#type(return_scroll)= <class 'NoneType'> ---- return_scroll= None

result4 = cursor.fetchmany(2)  #写数字2表示可以查询2条记录并且返回记录
print('type(result4) = %s --- result4 = %s' % (type(result4), result4))
#type(result4) = <class 'tuple'> --- result4 = ((3, '运维部'), (4, '财务部'))



#移动游标(1, mode= 'relative')以相对的路径从数据库记录的当前游标位置往后移动1行记录

return_scroll_2 = cursor.scroll(1, mode= 'relative')
print('type(return_scroll_2)= %s ---- return_scroll_2= %s' % (type(return_scroll_2), return_scroll_2))
#type(return_scroll_2)= <class 'NoneType'> ---- return_scroll_2= None

result33 = cursor.fetchall()    #可以查询所有剩余的记录
print('type(result33) = %s ------ result33 = %s' % (type(result33), result33))
#type(result33) = <class 'tuple'> ------ result33 = ((6, '销售部'), (7, '行政部'))


#对数据库表做修改操作,必须要commit提交
return_commit = conn.commit()

print('type(return_commit)= %s ---return_commit = %s' \
  % (type(return_commit), return_commit))
#type(return_commit)= <class 'NoneType'> ---return_commit = None

cursor.close()    #关闭游标
conn.close()      #关闭数据库pysql 连接

print(cursor , conn)
#<pymysql.cursors.Cursor object at 0x7f5cdf374588> <pymysql.connections.Connection object at 0x7f5cea1358d0>


print('type(conn) = %s , conn = %s ' % (type(conn), conn))
#type(conn) = <class 'pymysql.connections.Connection'> , conn = <pymysql.connections.Connection object at 0x7f5cea1358d0> 


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])


#[root@V0 devops_day02]# mysql  -uroot -p123  -e  "use pysql;desc  employees;"
#+--------------+-----------------------+------+-----+---------+-------+
#| Field        | Type                  | Null | Key | Default | Extra |
#+--------------+-----------------------+------+-----+---------+-------+
#| emp_id       | int(4)                | NO   | PRI | 0       |       |
#| emp_name     | varchar(20)           | NO   |     | NULL    |       |
#| gender       | enum('male','female') | YES  |     | NULL    |       |
#| birth_date   | date                  | NO   |     | NULL    |       |
#| phone_number | varchar(11)           | YES  |     | NULL    |       |
#| email        | varchar(50)           | YES  |     | NULL    |       |
#| dep_id       | int(4)                | YES  | MUL | NULL    |       |
#+--------------+-----------------------+------+-----+---------+-------+
#[root@V0 devops_day02]# mysql  -uroot -p123  -e  "use pysql;desc  departments;"
#+----------+-------------+------+-----+---------+-------+
#| Field    | Type        | Null | Key | Default | Extra |
#+----------+-------------+------+-----+---------+-------+
#| dep_id   | int(4)      | NO   | PRI | 0       |       |
#| dep_name | varchar(20) | NO   | UNI | NULL    |       |
#+----------+-------------+------+-----+---------+-------+
#[root@V0 devops_day02]# mysql  -uroot -p123  -e  "use pysql;desc  salary;"
#+---------+--------+------+-----+---------+----------------+
#| Field   | Type   | Null | Key | Default | Extra          |
#+---------+--------+------+-----+---------+----------------+
#| auto_id | int(4) | NO   | PRI | NULL    | auto_increment |
#| date    | date   | NO   |     | NULL    |                |
#| emp_id  | int(4) | YES  | MUL | NULL    |                |
#| basic   | int(4) | YES  |     | NULL    |                |
#| award   | int(4) | YES  |     | NULL    |                |
#+---------+--------+------+-----+---------+----------------+
#[root@V0 devops_day02]# 

#[root@V0 devops_day02]# mysql -uroot -p123 -e "use pysql;select *  from  employees;"
#+--------+----------+--------+------------+--------------+---------------+--------+
#| emp_id | emp_name | gender | birth_date | phone_number | email         | dep_id |
#+--------+----------+--------+------------+--------------+---------------+--------+
#|      1 | 张三     | male   | 1985-04-02 | 13302224455  | zhsan@163.com |      1 |
#|      2 | 李四     | male   | 1990-03-05 | 15099887766  | lisi@qq.com   |      1 |
#|      3 | 王五     | female | 2000-10-10 | 13802381238  | wgwu@qq.com   |      2 |
#+--------+----------+--------+------------+--------------+---------------+--------+
#[root@V0 devops_day02]# python3  pymysqltest.py
#.....................................
#[root@V0 devops_day02]# mysql -uroot -p123 -e "use pysql;select *  from  employees;"
#+--------+----------+--------+------------+--------------+---------------+--------+
#| emp_id | emp_name | gender | birth_date | phone_number | email         | dep_id |
#+--------+----------+--------+------------+--------------+---------------+--------+
#|      1 | 张三     | male   | 1985-04-02 | 13302224455  | zhsan@163.com |      1 |
#|      2 | 李四     | male   | 1990-03-05 | 15099887766  | lisi@qq.com   |      1 |
#|      3 | 王五     | female | 2000-10-10 | 13802381238  | wgwu@qq.com   |      2 |
#|      4 | bob      | male   | 1990-06-09 | 13802381238  | bob@qq.com    |      2 |
#|      5 | alice    | female | 1995-08-08 | 15851285125  | alice@qq.com  |      3 |
#+--------+----------+--------+------------+--------------+---------------+--------+
#[root@V0 devops_day02]# 



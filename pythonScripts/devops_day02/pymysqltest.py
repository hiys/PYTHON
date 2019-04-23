#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
"""
import  sys, pymysql
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

#创建连接conn,访问数据库pysql
conn =  pymysql.connect(
#  host = '192.168.1.10',  #具体的ip地址不允许空密码匿名用户存在
  host = '192.168.0.10', #具体的ip地址不允许空密码匿名用户存在
#  host = '127.0.0.10',   #127.0.0.10允许空密码匿名用户存在
  port = 3306,
  user = 'root',
  passwd = '123',
  db = 'pysql',
  charset = 'utf8'
)

cursor  = conn.cursor()  #创建游标
print('type(cursor) = %s , cursor = %s ' % (type(cursor), cursor))
#type(cursor) = <class 'pymysql.cursors.Cursor'> , cursor = <pymysql.cursors.Cursor object at 0x7f421d59b5f8> 


#sql_insert1 = "insert into departments values (%s, %s)" #注意只能是字符串类型%s,不是数字%d
#------------------cursor.execute() ----- 只执行一条语句---
#result = cursor.execute(sql_insert1, (7, '行政部'))
#print('type(result) = %s ------ result = %d' % (type(result), result))


#注意values (%s, %s, %s, %s, %s, %s, %s)" 只能是字符串类型%s,不是数字%d
sql_insert2 = "insert into employees   values (%s, %s, %s, %s, %s, %s, %s)"
employees = [
  (4, 'bob', 'male', '1990-06-09', '13802381238', 'bob@qq.com', 2),
  (5, 'alice', 'female', '1995-08-08', '15851285125', 'alice@qq.com', 3)
]
#注意变量 employees 是个列表类型
#-----------cursor.executemany() ----- 执行多条语句---
result2 = cursor.executemany(sql_insert2, employees)

print('type(result2) = %s ------ result2 = %d' % (type(result2), result2))
#type(result2) = <class 'int'> ------ result2 = 2


sql_select = 'select dep_id, dep_name  from  departments where dep_name= %s'
result3 = cursor.execute(sql_select, ('财务部',))
print('type(result3) = %s ------ result3 = %d' % (type(result3), result3))
#type(result3) = <class 'int'> ------ result3 = 1

#对数据库表做修改操作,必须要commit提交
conn.commit()


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
#__name__ is __main__
#type(cursor) = <class 'pymysql.cursors.Cursor'> , cursor = <pymysql.cursors.Cursor object at 0x7f421d59b5f8> 
#type(result2) = <class 'int'> ------ result2 = 2
#type(result3) = <class 'int'> ------ result3 = 1
# sys.argv[0]  is pymysqltest.py
#
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



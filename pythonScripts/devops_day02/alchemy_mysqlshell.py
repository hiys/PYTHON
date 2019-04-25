#!/usr/bin/env python3
#coding:UTF-8
"""#coding=UTF-8
"""

import  sys,  subprocess
from  alchemy_ORM  import  Departments, Employees, Salary, session
from  sqlalchemy   import  and_,  or_


sqlcmd="\"\
SELECT departments.dep_id , departments.dep_name  \
FROM departments  \
WHERE departments.dep_name = '人力部';\""


mysqlshell= "mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  %s" %  sqlcmd

print('------------------------------')
print(mysqlshell)
print('------------------------------')

#------------------------------
#mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  "SELECT departments.dep_id , departments.dep_name  FROM departments  WHERE departments.dep_name = '人力部';"
#------------------------------


rcmd = subprocess.call(mysqlshell, shell = True)

if rcmd == 0:
  print('-----select  well done ---- rcmd  --------\n')
else:
  print('----- rcmd = %d -------\n' % rcmd)


#------------------------------
#mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e  "SELECT departments.dep_id , departments.dep_name  FROM departments  WHERE departments.dep_name = '人力部';"
#------------------------------
#+--------+-----------+
#| dep_id | dep_name  |
#+--------+-----------+
#|      1 | 人力部    |
#+--------+-----------+
#-----select  well done ---- rcmd  --------



if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])



#[root@V0 devops_day02]# sqlcmd="
#> SELECT departments.dep_id , departments.dep_name
#> FROM departments 
#> WHERE departments.dep_name ='人力部';"
#[root@V0 devops_day02]# 
#[root@V0 devops_day02]# echo  $sqlcmd
#SELECT departments.dep_id , departments.dep_name FROM departments WHERE departments.dep_name ='人力部';
#[root@V0 devops_day02]# 
#[root@V0 devops_day02]# mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e "$sqlcmd"
#+--------+-----------+
#| dep_id | dep_name  |
#+--------+-----------+
#|      1 | 人力部    |
#+--------+-----------+
#[root@V0 devops_day02]# 
#[root@V0 devops_day02]# mysqlshell="mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy  -e \"$sqlcmd\""
#[root@V0 devops_day02]# 
#[root@V0 devops_day02]# echo $mysqlshell
#mysql -uroot -p123 -h192.168.0.11 -P3306 -D alchemy -e " SELECT departments.dep_id , departments.dep_name FROM departments WHERE departments.dep_name ='人力部';"
#[root@V0 devops_day02]# 



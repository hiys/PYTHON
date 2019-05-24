from myorm import Departments, Employees, Salary, session
from datetime import datetime

dep_ops = Departments(dep_name='运维部')
dep_finance = Departments(dep_name='财务部')
dep_market = Departments(dep_name='市场部')
emp_alice = Employees(
    emp_name='alice',
    gender='female',
    phone='15088990022',
    email='alice@tedu.cn',
    dep_id=1
)
emp_zs = Employees(
    emp_name='张三',
    gender='male',
    phone='13412345678',
    email='zhangsan@tedu.cn',
    dep_id=2
)
emp_ls = Employees(
    emp_name='李四',
    gender='male',
    phone='13800998877',
    email='lisi@tedu.cn',
    dep_id=2
)
emp_ww = Employees(
    emp_name='王五',
    gender='male',
    phone='15098283828',
    email='wangwu@tedu.cn',
    dep_id=2
)
emp_zl = Employees(
    emp_name='赵六',
    gender='male',
    phone='13709762831',
    email='zhaoliu@tedu.cn',
    dep_id=3
)
sal_bob_201803 = Salary(
    emp_id = 1,
    date=datetime.date(datetime.now()),
    basic=10000,
    award=5000
)
sal_bob_201802 = Salary(
    emp_id = 1,
    date='2018-03-10',
    basic=10000,
    award=4500
)
sal_alice_201802 = Salary(
    emp_id = 2,
    date='2018-03-10',
    basic=11000,
    award=5500
)
sal_alice_201803 = Salary(
    emp_id = 2,
    date='2018-04-10',
    basic=11000,
    award=4000
)
sal_zs_201802 = Salary(
    emp_id = 3,
    date='2018-03-10',
    basic=9000,
    award=4500
)
sal_zs_201803 = Salary(
    emp_id = 3,
    date='2018-04-10',
    basic=9000,
    award=3500
)

session.add_all([dep_ops, dep_finance, dep_market])
session.commit()
session.add_all([emp_alice, emp_zs, emp_ls, emp_ww, emp_zl])
session.commit()
session.add_all([sal_bob_201802, sal_bob_201803, sal_alice_201802, sal_alice_201803, sal_zs_201802, sal_zs_201803])
session.commit()

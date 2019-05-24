from myorm import Departments, Salary, Employees, session

# select  * from departments order by dep_id limit 1, 3;?
for row in session.query(Departments).order_by(Departments.dep_id)[1:4]:
    print(row.dep_id, row.dep_name)

# select * from departments where dep_id=2;
for row in session.query(Departments).filter(Departments.dep_id==2):
    print(row.dep_id, row.dep_name)

# select * from salary where award>4000 and basic>10000;
for row in session.query(Salary).\
    filter(Salary.award>4000).filter(Salary.basic>10000):
    print(row.emp_id, row.basic, row.award)

# select * from employees where emp_name like '李%';
for row in session.query(Employees).\
        filter(Employees.emp_name.like('李%')):
    print(row.emp_name)

# select * from employees where emp_name like '李_';
for row in session.query(Employees).\
        filter(Employees.emp_name.like('李_')):
    print(row.emp_name)

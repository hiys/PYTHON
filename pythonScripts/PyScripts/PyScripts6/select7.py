from myorm import Employees, Departments, Salary, session

# select count(*) from employees;
print(session.query(Employees).count())

# select e.emp_name, d.dep_name from employees as e join departments as d on e.dep_id=d.dep_id;
q = session.query(Employees.emp_name, Departments.dep_name).\
    join(Departments, Employees.dep_id==Departments.dep_id)
print(q.all())

q2 = session.query(Employees.emp_name, Salary.date, Salary.basic+Salary.award).\
    join(Salary, Employees.emp_id==Salary.emp_id)
print(q2.all())

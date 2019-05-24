from myorm import Departments, Employees, session

# select * from departments
for instance in session.query(Departments):
    print(instance)
    print(instance.dep_id, ':', instance.dep_name)

# select * from departments order by dep_id
for instance in session.query(Departments).order_by(Departments.dep_id):
    print(instance.dep_id, ':', instance.dep_name)

# select emp_name, phone from employees;
for name, phone in session.query(Employees.emp_name, Employees.phone):
    print('%s: %s' % (name, phone))

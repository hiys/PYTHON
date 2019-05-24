from myorm import Employees, session

# select * from employees where emp_name='bob' or emp_name='alice';
# select * from employees where emp_name in ('bob', 'alice');
for row in session.query(Employees).\
        filter(Employees.emp_name.in_(['bob', 'alice'])):
    print(row.emp_name, row.phone)

# select * from employees where emp_name not in ('bob', 'alice');
for row in session.query(Employees).\
        filter(~Employees.emp_name.in_(['bob', 'alice'])):
    print(row.emp_name, row.phone)

# select * from employees where phone is null;
for row in session.query(Employees).\
    filter(Employees.phone.is_(None)):
    print(row.emp_name)

# select * from employees where phone is not null;
for row in session.query(Employees).\
    filter(Employees.phone.isnot(None)):
    print(row.emp_name)

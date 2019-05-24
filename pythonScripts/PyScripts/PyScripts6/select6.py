from myorm import Employees, session

# all返回的是列表
result = session.query(Employees.emp_name, Employees.phone).all()
print(result)

# first返回符合条件的第一个记录
result = session.query(Employees.emp_name, Employees.phone).\
    filter(Employees.emp_name.like('李%')).first()
print(result)

# one要求查询只能有一条记录，否则报错
result = session.query(Employees.emp_name, Employees.phone).\
    filter(Employees.emp_name.like('李__')).one()
print(result)

#calar调用one，返回第一列
result = session.query(Employees.emp_name, Employees.phone).\
    filter(Employees.emp_name.like('李__')).scalar()
print(result)

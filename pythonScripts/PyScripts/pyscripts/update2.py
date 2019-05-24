from myorm import Departments, session

q = session.query(Departments).get(1)  # get的参数是表的主键
q.dep_name = 'HR'
session.commit()


from myorm import Departments, session

q = session.query(Departments).filter(Departments.dep_name=='人事部')
q.update({Departments.dep_name: '人力资源部'})
session.commit()



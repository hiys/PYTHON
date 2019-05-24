from myorm import Departments, session

q = session.query(Departments).get(4)
session.delete(q)
session.commit()

# dep_finance = Departments(dep_name='财务部', dep_id=4)
# session.add(dep_finance)
# session.commit()

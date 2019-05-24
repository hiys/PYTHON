from sqlalchemy_conn import Departments, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
session = Session(bind=engine)

hr = Departments(dep_name='hr')
print(hr)
print(hr.dep_name)
print(hr.dep_id)
session.add(hr)
session.commit()
print(hr.dep_id)

from sqlalchemy_conn import Departments, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
session = Session(bind=engine)

dep_dev = Departments(dep_name='开发部')
dep_ops = Departments(dep_name='运维部')
session.add_all([dep_dev, dep_ops])
session.commit()

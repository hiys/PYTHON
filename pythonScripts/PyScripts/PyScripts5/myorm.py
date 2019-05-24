from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root:tedu.cn@localhost/tedu?charset=utf8',
    encoding='utf8',
    echo=True
)
Base = declarative_base()  # 创建映射类的基类
Session = sessionmaker()
session = Session(bind=engine)

class Departments(Base):
    __tablename__ = 'departments'  # 在tedu数据库中创建的表名
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)
    def __str__(self):
        return '<Department(dep_name=%s)>' % self.dep_name

class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20), nullable=False)
    gender = Column(String(10))
    phone = Column(String(11))
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))
    def __str__(self):
        return '<Eployee(emp_name=%s)>' % self.emp_name

class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    date = Column(Date)
    basic = Column(Integer)
    award = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)

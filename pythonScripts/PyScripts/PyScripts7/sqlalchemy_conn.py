# 1、安装　
# [root@room8pc16 db2]# pip3 install sqlalchemy
# [root@room8pc16 db2]# pip3 install pymysql
# 2、使用sqlalchemy，先要创建数据库
# 数据库名为tedu，缺省使用的字符集是utf8
# MariaDB [tarena]> CREATE DATABASE tedu DEFAULT CHARSET utf8;

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# root:tedu.cn  是用冒号分开的用户名和密码
# localhost 是mysql数据库服务器的地址  tedu是数据库名
# echo=True 表示在屏幕上显示日志
engine = create_engine(
    'mysql+pymysql://root:tedu.cn@localhost/tedu?charset=utf8',
    encoding='utf8',
    echo=True
)
Base = declarative_base()  # 创建映射类的基类

class Departments(Base):
    __tablename__ = 'departments'  # 在tedu数据库中创建的表名
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)
    def __str__(self):
        return '<Department(dep_name=%s)>' % self.dep_name

if __name__ == '__main__':
    Base.metadata.create_all(engine)

# >>> user1 = collections.namedtuple('user1', ['name', 'age'])
# >>> bob = user1('Bob Green', 25)
# >>> bob[0]
# 'Bob Green'
# >>> bob[1]
# 25
# >>> bob.name
# 'Bob Green'
# >>> bob.age
# 25
from myorm import Departments, session

for row in session.query(Departments, Departments.dep_name):
    print(row.dep_name)

# select dep_name as 部门 from departments;
for row in session.query(Departments.dep_name.label('部门')):
    print(row.部门)

# select * from departments order by dep_id
for row in session.query(Departments).order_by(Departments.dep_id):
    print(row.dep_id, row.dep_name)

# select * from departments order by dep_id desc;
for row in session.query(Departments).order_by(Departments.dep_id.desc()):
    print(row.dep_id, row.dep_name)

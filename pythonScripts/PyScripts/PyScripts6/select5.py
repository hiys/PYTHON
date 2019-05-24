from myorm import Salary, session
from sqlalchemy import and_, or_

# select * from salary where award>4500 and basic>10000;
for row in session.query(Salary).\
        filter(and_(Salary.award>4500, Salary.basic>10000)):
    print(row.emp_id, row.basic, row.award)

# select * from salary where basic>10000 or award>4500;
for row in session.query(Salary).\
    filter(or_(Salary.basic>10000, Salary.award>4500)):
    print(row.emp_id, row.basic, row.award)

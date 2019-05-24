import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='tarena',
    charset='utf8'
)

cursor = conn.cursor()  # 创建游标
sql_insert1 = "INSERT INTO departments VALUES (%s, %s)"
# result = cursor.execute(sql_insert1, (7, '行政部'))

sql_insert2 = "INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s, %s)"
employees = [
    (3, 'bob', 'male', '1990-06-08', '15988776655', 'bob@tedu.cn', 2),
    (4, 'alice', 'female', '1995-10-23', '13300998877', 'alice@tedu.cn', 2),
]
cursor.executemany(sql_insert2, employees)

conn.commit()
cursor.close()
conn.close()


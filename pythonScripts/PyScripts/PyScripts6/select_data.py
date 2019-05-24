import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='tarena',
    charset='utf8'
)

cursor = conn.cursor()
sql_select1 = "SELECT * FROM departments ORDER BY dep_id"
cursor.execute(sql_select1)
result1 = cursor.fetchone()
print(result1)
result2 = cursor.fetchmany(2)
print(result2)
result3 = cursor.fetchall()
print(result3)
cursor.close()
conn.close()

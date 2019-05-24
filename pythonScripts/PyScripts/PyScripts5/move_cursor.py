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
cursor.scroll(3, mode='absolute')
result = cursor.fetchmany(3)
print(result)
cursor.close()
conn.close()



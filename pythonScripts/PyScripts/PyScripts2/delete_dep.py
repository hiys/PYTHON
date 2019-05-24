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
sql_del = "DELETE FROM departments WHERE dep_name='finance'"
cursor.execute(sql_del)
conn.commit()
cursor.close()
conn.close()



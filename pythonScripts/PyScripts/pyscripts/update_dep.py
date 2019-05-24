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
sql_update = "UPDATE departments SET dep_name='finance' WHERE dep_name='财务部'"
cursor.execute(sql_update)
conn.commit()
cursor.close()
conn.close()



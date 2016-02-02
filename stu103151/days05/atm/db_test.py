import MySQLdb as mdb
import pymysql
conn = pymysql.connect(user='root',
                       passwd='jack',
                       host='localhost',
                       db='atm')
cur = conn.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print("Database version : %s " % data)
#cur.execute("create table user(id int ,name varchar(20),class varchar(30),age varchar(10))")
#sqli="insert into USER values(%s,%s,%s,%s)"
'''
cur.executemany(sqli,[
    ('3','Tom','1 year 1 class','6'),
    ('3','Jack','2 year 1 class','7'),
    ('3','Yaheng','2 year 2 class','7'),
    ])
'''
aa=cur.execute("select * from USER ")
print(aa)
info = cur.fetchmany(aa)
for ii in info:
    print(ii)
cur.close()
conn.commit()
conn.close()
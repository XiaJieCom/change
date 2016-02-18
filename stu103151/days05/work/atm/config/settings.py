import pymysql
def auth_db():
    try:
        conn = pymysql.connect(user='root',passwd='jack',host='localhost',db='atm')
        cur = conn.cursor()
        cur.execute("SELECT VERSION()")
        data = cur.fetchone()
        print("Database version : %s " % data)
        #return auth_db()
        return True
    except pymysql.connector.Error as e:
        print ('Error : {}'.format(e));

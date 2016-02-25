import pymysql,sys,os

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
print(parentdir)
#初始化参数
def init():
    global DATABASE_NAME
    DATABASE_NAME = 'game'
    global HOST
    HOST = 'localhost'
    global PORT
    PORT = '3306'
    global USER_NAME
    USER_NAME = 'game'
    global PASSWORD
    PASSWORD = '123'
    global CHAR_SET
    CHAR_SET = 'utf8'
#获取数据库连接
def get_conn():
    init()
    return (pymysql.connect(host = HOST, user = USER_NAME, passwd = PASSWORD, db = DATABASE_NAME, charset = CHAR_SET))
#获取游标
def get_cursor(conn):
    return conn.cursor()
#关闭连接
def conn_close(conn):
    if conn != None:
        conn.close()
#关闭游标
def cursor_close(cursor):
    if cursor != None:
        cursor.close()
#关闭所有
def close(cursor, conn):
    cursor_close(cursor)
    conn_close(conn)

def select_all(table_name):
    sql = 'select id,name from ' + table_name
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql)
    for row in cursor.fetchall():
        print(row[0],row[1])
def select_equipment(table_name,id):
    sql = "select name from "+ table_name +" where id = %s"
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql % id)
    return cursor.fetchone()
def select_equipment_power(table_name,column):
    sql = "select power from "+ table_name +" where name = %s"
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,column)
    return cursor.fetchone()












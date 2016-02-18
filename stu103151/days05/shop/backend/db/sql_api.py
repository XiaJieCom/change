import pymysql
#初始化参数
def init():
    global DATABASE_NAME
    DATABASE_NAME = 'shop'
    global HOST
    HOST = 'localhost'
    global PORT
    PORT = '3306'
    global USER_NAME
    USER_NAME = 'root'
    global PASSWORD
    PASSWORD = 'jack'
    global CHAR_SET
    CHAR_SET = 'utf8'

#获取数据库连接
def get_conn():
    init()
    return (pymysql.connect(host = HOST, user = USER_NAME, passwd = PASSWORD, db = DATABASE_NAME, charset = CHAR_SET))
#获取游标
    cursorclass = pymysql.cursors.DictCursor
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


def select_all():
    sql = 'select * from goods'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql)
    cursorclass = pymysql.cursors.DictCursor
    for row in cursor.fetchall():
        id = row[0]
        name = row[1]
        price = row[2]
        print('%s   %s  %s'% (row[0],row[1],row[2]))
        #print(row[0],row[1],row[2])
def select_price(id):
    sql = 'select price from goods WHERE id = %s'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,id)
    cursorclass = pymysql.cursors.DictCursor
    return list(cursor.fetchone())















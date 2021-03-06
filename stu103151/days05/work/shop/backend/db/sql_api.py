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
def select_name(id):
    sql = 'select name from goods WHERE id = %s'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,id)
    cursorclass = pymysql.cursors.DictCursor
    return list(cursor.fetchone())
def insert(name,passwd,account,mail,status,date):
      sql = 'insert into user(name,passwd,account,mail,status,create_time) values(%s,%s,%s,%s,%s,%s)'
      values = [name,passwd,account,mail,status,date]
      conn = get_conn()
      cursor = get_cursor(conn)
      result = cursor.execute(sql,values)
      conn.commit()
      close(cursor, conn)
      return result
def active(name):
    sql = 'select status from user where name = %s and status = 1'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,name)
    if result == 0:
        return True
    else:
        return False
def auth(name,passwd):
    data = name,passwd
    sql = 'SELECT NAME,account from USER WHERE NAME = (%s) and passwd = (%s)'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,data)
    conn.commit()
    close(cursor, conn)
    if result != 0:
        return True
def account(name):
    sql = 'select account from USER where name = %s'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,name)
    if result == 0:
        return False
    else:
        return cursor.fetchone()
def clock_account(name):
    sql = 'update USER set status = 1  where name = %s'
    data = name
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,data)
    conn.commit()
    close(cursor, conn)
    return result












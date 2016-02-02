import pymysql
#初始化参数
def init():
    global DATABASE_NAME
    DATABASE_NAME = 'atm'
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

def auth(name,passwd):
    v1=name
    v2=passwd
    sql = 'SELECT NAME,account from USER WHERE NAME = (%s) and passwd = (%s)'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,(v1,v2))
    conn.commit()
    close(cursor, conn)
    if result != 0:
        return True
def insert(name,passwd,account,mail):
      sql = 'insert into user(name,passwd,account,mail) values(%s,%s,%s,%s)'
      values = [name,passwd,account,mail]
      conn = get_conn()
      cursor = get_cursor(conn)
      result = cursor.execute(sql, values)
      conn.commit()
      close(cursor, conn)
      return result
def select(name):
    sql = 'select name,account,amount from USER where name = %s'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,name)
    return cursor.fetchone()[2]
def select_name(i_account):
    sql = 'select name,account from USER where account = %s'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,i_account)
    return cursor.fetchone()[0]

def update(name,new_amount):
    #sql = "update user set amount = '%s'  where name = '%s'"%(name,new_amount)
    sql = 'update user set amount = %s  where name = %s'
    data = new_amount,name
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,data)
    conn.commit()
    close(cursor, conn)
    return result














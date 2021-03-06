import pymysql,sys,os

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
print(parentdir)
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
    data = name,passwd
    sql = 'SELECT NAME,account from USER WHERE NAME = (%s) and passwd = (%s)'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,data)
    conn.commit()
    close(cursor, conn)
    if result != 0:
        return True
def s_auth(account,passwd):
    data = account,passwd
    sql = 'SELECT account from USER WHERE account = %s and passwd = %s'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,data)
    conn.commit()
    close(cursor, conn)
    if result != 0:
        return True
def active(name):
    sql = 'select status from user where name = %s and status = 1'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,name)
    if result == 0:
        return True
    else:
        return False
def role(name):
    sql = 'select role from user where name = %s and role = "admin"'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,name)
    if result == 0:
        return True
    else:
        return False

def insert(name,passwd,account,amount,mail,status,date):
      sql = 'insert into user(name,passwd,account,amount,mail,status,create_time) values(%s,%s,%s,%s,%s,%s,%s)'
      values = [name,passwd,account,amount,mail,status,date]
      conn = get_conn()
      cursor = get_cursor(conn)
      result = cursor.execute(sql,values)
      conn.commit()
      close(cursor, conn)
      return result
def select(name):
    sql = 'select name,account,amount from USER where name = %s'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,name)
    return cursor.fetchone()[2]
def select_amount(account):
    sql = 'select amount from USER where account = %s'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,account)
    return cursor.fetchone()
def select_name(i_account):
    sql = 'select name,account from USER where account = %s'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,i_account)
    if result == 0:
        return False
    else:
        return cursor.fetchone()[0]
def update(name,new_amount):
    #sql = "update user set amount = '%s'  where name = '%s'"%(name,new_amount)
    sql = 'update USER set amount = %s  where name = %s'
    data = new_amount,name
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,data)
    conn.commit()
    close(cursor, conn)
    return result
def up_amount(account,amount):
    sql = 'update USER set amount = %s  where account = %s'
    data = amount,account
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,data)
    conn.commit()
    close(cursor, conn)
    return result
def clock_account(name):
    sql = 'update USER set status = 1  where name = %s'
    data = name
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,data)
    conn.commit()
    close(cursor, conn)
    return result
def select_all():
    sql = 'select name,account,status from USER'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql)
    for row in cursor.fetchall():
        print(row[0],row[1],row[2])
        #for r in row:
        #    print(r)
    close(cursor,conn)
def update_clock(account,status):
    sql = 'update USER set status = %s  where account = %s'
    data = status,account
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,data)
    conn.commit()
    close(cursor, conn)
    return result
def del_user(account):
    sql = 'delete from User where account = %s'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,account)
    conn.commit()
    close(cursor, conn)
    return result
def log(name,date,event):
      sql = 'insert into log(name,event,date) values(%s,%s,%s)'
      values = [name,event,date]
      conn = get_conn()
      cursor = get_cursor(conn)
      result = cursor.execute(sql,values)
      conn.commit()
      close(cursor, conn)
      return result
def select_log(name):
    sql = 'select * from log WHERE NAME = %s'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,name)
    for row in cursor.fetchall():
        print(row[2],row[3])

'''

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
'''













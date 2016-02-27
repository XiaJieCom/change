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
    '''
    查询某张表的 ID/name/money 信息
    :param table_name:
    :return: ID/name/money
    '''
    sql = 'select id,name,money from ' + table_name
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql)
    for row in cursor.fetchall():
        print(row[0],row[1],row[2])
def select_equipment(table_name,id):
    '''
    查询某张表的 name 根据ID
    :param table_name:
    :param id:
    :return: name
    '''
    sql = "select name from "+ table_name +" where id = %s"
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql % id)
    return cursor.fetchone()
def select_equipment_power(table_name,column):
    '''
    查询某表的 power 根据表名和name
    :param table_name:
    :param column:
    :return: power
    '''
    sql = "select power from "+ table_name +" where name = %s"
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql,column)
    return cursor.fetchone()












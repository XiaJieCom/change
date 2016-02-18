from backend.db import sql_api


def select_all():
    func = sql_api.select_all()
    return func
def select_price(id):
    func = sql_api.select_price(id)
    return func
def select_name(id):
    func = sql_api.select_name(id)
    return func
def reg(name,passwd,account,mail,status,date):
    insert_data = sql_api.insert(name,passwd,account,mail,status,date)
    print("您的用户名: %s\n邮箱地址: %s\n注册成功!"%(name,mail))
def active(name):
    func = sql_api.active(name)
    return func


'''
def update_amount(name,new_amount):
    func = sql_api.update(name,new_amount)
    return func
'''
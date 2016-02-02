from backend.db import sql_api


def reg(name,passwd,account,mail):
    insert_data = sql_api.insert(name,passwd,account,mail)
    print("您的用户名: %s\n卡号: %s\n邮箱地址: %s\n开卡成功!"%(name,account,mail))
def login(name,passwd):
    login_data = sql_api.auth(name,passwd)
    return login_data

def amount(name):
    amount_data = sql_api.select(name)
    return amount_data
def account(i_account):
    q_name = sql_api.select_name(i_account)
    return q_name
def update_amount(name,new_amount):
    func = sql_api.update(name,new_amount)
    return func
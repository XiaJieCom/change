import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from atm.backend.db import sql_api as atm


def reg(name,passwd,account,amount,mail,status,date):
    insert_data = sql_api.insert(name,passwd,account,amount,mail,status,date)
    print("您的用户名: %s\n卡号: %s\n当前余额: %s$\n邮箱地址: %s\n开卡成功!"%(name,account,amount,mail))

def s_login(account,passwd):
    func = atm.s_auth(account,passwd)
    return func

def q_amount(account):
    func = atm.select_amount(account)
    return func

def up_amount(account,amount):
    func = atm.up_amount(account,amount)
    return func




#import backend.db.sql_api as sql_api
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from atm.backend.db import sql_api as atm


def reg(name,passwd,account,amount,mail,status,date):
    insert_data = sql_api.insert(name,passwd,account,amount,mail,status,date)
    print("您的用户名: %s\n卡号: %s\n当前余额: %s$\n邮箱地址: %s\n开卡成功!"%(name,account,amount,mail))
def active(name):
    print(parentdir)
    func = sql_api.active(name)
    return func
def login(name,passwd):
    func = sql_api.auth(name,passwd)
    return func
def s1_login(account,passwd):
    func = sql_api.s_auth(account,passwd)
    return func
def s_login(account,passwd):
    func = atm.s_auth(account,passwd)
    return func
def role(name):
    func = sql_api.role(name)
    return func
def clock(name):
    clock_data = sql_api.update(name)

def amount(name):
    func = sql_api.select(name)
    return func
def q_amount(account):
    func = atm.select_amount(account)
    return func
def account(i_account):
    func = sql_api.select_name(i_account)
    return func

def update_amount(name,new_amount):
    func = sql_api.update(name,new_amount)
    return func
def up_amount(account,amount):
    func = atm.up_amount(account,amount)
    return func
def clock_account(name):
    func = sql_api.clock_account(name)
    return func
def select_all():
    func = sql_api.select_all()
    return func
def update_clock(account,status):
    func = sql_api.update_clock(account,status)
    return func
def del_user(account):
    func = sql_api.del_user(account)
    return func
def log(name,date,event):
    func = sql_api.log(name,date,event)
    return func
def select_log(name):
    func = sql_api.select_log(name)
    return func

def ts():
    print('ss')


'''
def update_amount(name,new_amount):
    func = sql_api.update(name,new_amount)
    return func
'''
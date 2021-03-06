
import backend.db.sql_api as sql_api
import os,sys


#开卡注册
def reg(name,passwd,account,amount,mail,status,date):
    insert_data = sql_api.insert(name,passwd,account,amount,mail,status,date)
    print("您的用户名: %s\n卡号: %s\n当前余额: %s$\n邮箱地址: %s\n开卡成功!"%(name,account,amount,mail))
#根据用户名判断状态
def active(name):
    func = sql_api.active(name)
    return func
#登录验证
def login(name,passwd):
    func = sql_api.auth(name,passwd)
    return func
#判断角色
def role(name):
    func = sql_api.role(name)
    return func
#锁定用户
def clock(name):
    clock_data = sql_api.update(name)
#根据用户名查询余额
def amount(name):
    func = sql_api.select(name)
    return func
#根据卡号查询用户名
def account(i_account):
    func = sql_api.select_name(i_account)
    return func
#更新额度
def update_amount(name,new_amount):
    func = sql_api.update(name,new_amount)
    return func
#锁定账号
def clock_account(name):
    func = sql_api.clock_account(name)
    return func
#查询所有用户信息
def select_all():
    func = sql_api.select_all()
    return func
#解锁
def update_clock(account,status):
    func = sql_api.update_clock(account,status)
    return func
#用户注销
def del_user(account):
    func = sql_api.del_user(account)
    return func
#操作日志
def log(name,date,event):
    func = sql_api.log(name,date,event)
    return func
#查询用户操作日志
def select_log(name):
    func = sql_api.select_log(name)
    return func

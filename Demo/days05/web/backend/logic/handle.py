from backend.db.sql_api import select
def home():
    print('This is home!')
    q_data = select('user','sss')
    print('res:',q_data)
def tv():
    print('This is tv!')
def movie():
    print('This is movie!')
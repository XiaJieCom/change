from config import settings
import os
#base_dir =os.path.abspath(__file__)
#print(base_dir)
def db_auth(configs):
    if configs.database['user'] == 'root' and configs.database['passwd'] == '123':
        print('DB connection successful!')
        return True
    else:
        print('UserName or Passwd was wrong...')

def select(table,column):
    if db_auth(settings):
        if table == 'user':
            user_info = {
                '01':['tom',10,'cat'],
                '02':['jack',10,'cow']
            }
            return user_info

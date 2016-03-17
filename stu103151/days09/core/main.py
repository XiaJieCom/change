
#from core import config_handler
import os,sys
from db import userdb
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Salt(object):
    def __init__(self):
        self.login_name = None

        #如果登录成功,那么就执行menu函数
        if self.login():
            self.menu()
    #登录程序
    def login(self):
        #错误三次自动退出
        count = 0
        while count < 3:
            #输入name,如果为空,继续
            u_name = input('Please input your name: ').strip()
            if len(u_name) == 0:continue
            #输入passwd,如果为空,继续
            u_passwd = input('Please input your password: ').strip()
            if len(u_passwd) ==0:continue
            #从userdb,取出字典USER_ACCOUN,里面对应的name和passwd,如果匹配,那么就返回True,否则返回False
            if u_name in userdb.USER_ACCOUNT:
                if userdb.USER_ACCOUNT[u_name]['passwd'] == u_passwd:
                    self.login_name == u_name
                    return True
                else:
                    print('valid username or password!')
                    count += 1
            else:
                print('valid username or password!')
                count += 1
        return False
    def menu(self):
        print('This is menu')




        exit()
def run():
    run = Salt()

if __name__ == '__main__':
    host = Salt()
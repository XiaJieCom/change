
#from core import config_handler
import os,sys
from db import userdb
from core import config_handle
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
        cmd = input('>> ').strip()
        self.transfer_cmd(cmd)
    def show(self,transfer_cmd):
        '''
        输出分组信息等等
        :param transfer_cmd:
        :return:
        '''
        print('This is all of hosts: ')
        configure = config_handle.read()
        #从config_handle读取分组信息
        if len(transfer_cmd) == 1:
            #如果只输入了'show'打印所有分组信息
            print("{:*^50}".format("groups"))
            #print(configure)
            for k in configure:
                #循环打印读取字典的key,也就是分组组名
                print(k)
            print("*" * 50)
        elif '-g' in transfer_cmd:
            #如果用户输入带有'-g',说明指定了分组
            group_list = transfer_cmd[transfer_cmd.index("-g")+1:]
            #获取组名,用户输入信息,'-g' 下标后面的字符 就是组名,赋给 group_list这个列表
            print(group_list)
            try:
                for i in group_list:
                    print("{:*^50}".format(i))
                    for j in configure[i]:
                        print(j)
                    print("*" * 50)
            except (ValueError, KeyError):
                print("invalid group name!")
        else:
            print("invalid instructions!")
    def add(self,transfer_cmd):
        add_flag = True
        print('This is add,example add -g xxx -h x.x.x.x')
        #print(transfer_cmd.index["-g"])

        if len(transfer_cmd) < 5:
            #如果输入不小于5,说明格式不对
            print('格式错误请重试')
        else:
            if add_flag:
                index_g = transfer_cmd.index('-g')
                #判断出 '-g'的下标,以便取出组名
                #print(index_g)
                index_h = transfer_cmd.index('-h')
                #判断出'-h'的下标,以便取出后面的主机地址
                #print(index_h)
                group = transfer_cmd[index_g+1:index_h]
                #将组名加入group_list,组名就等于 index_g+1:index_h 之间的值
                print(group)
                host_list = transfer_cmd[index_h+1:]
                #将下标为index_h+1后面的元素放入host_list,为主机地址列表
                print(host_list)
                host = config_handle.read()
                for i in host:
                    if i in host.keys():
                        #host.keys().append(host_list)
                        pass
                    else:
                        raw = input('你想新建一个分组吗? [y/n]').strip()
                        if raw == 'y':
                            host[i] = host_list
                            print(host)
                            config_handle.write(host)
                        else:
                            print('那就返回吧 !')







    def delete(self,transfer_cmd):
        print('This is delete')

    def transfer_cmd(self,cmd):
        '''
        用于处理分割输入的命令
        :param cmd:
        :return:
        '''
        cmd_list = cmd.split()
        try:
            func_str = cmd_list[0]
            #取出第一个元素,判断该命令是否对照指定函数,如果不存在,提示错误
            if hasattr(self, func_str):
                func = getattr(self, func_str)
                func(cmd_list)
            else:
                print("Invalid instruction...")
        except IndexError as e:
            print('IndexError')




def run():
    run = Salt()

if __name__ == '__main__':
    host = Salt()
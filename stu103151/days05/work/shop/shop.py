import random,time,datetime,sys,os

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from backend.logic import handle

from atm.backend.logic import shop_handle as atm

def welcome():
    res = ''.center(100,'#')
    return print(res)
def create_name():
    r_name = ''
    for i in range(4):
        current = random.randrange(0,4)
        if current != i:
            temp = chr(random.randint(65,90))
        else:
            temp = random.randint(0,9)
        r_name += str(temp)
    return r_name
def create_mail():
    random_num = random.randint(11111111111,99999999999)
    res =str(random_num)  + '@163.com'
    return res

def create_date():
    c_date = datetime.datetime.now()
    return c_date
def reg_user():
    i_name = input('Input your name: ').strip()
    i_passwd = input('Input your passwd: ').strip()
    i_mail = create_mail()
    #i_account = str(random.randint(6200000000000000,6299999999999999))
    i_account = '6282781692694856'
    #i_amount = random.randint(0,99999999)
    i_status = 0
    i_date = create_date()
    handle.reg(i_name,i_passwd,i_account,i_mail,i_status,i_date)

def log(name,event):
    date = create_date()
    handle.log(name,date,event)


#欢迎信息
def welcome(hello):
    res = hello.center(100,'*')
    return print(res)
choice_list = []
choice_name_list = []

if __name__ == '__main__':
    welcome("欢迎登录网上商城，祝您购物愉快！")
    #循环展示商品,用户输入购买选项
    while True:
        handle.select_all()
        user_choice = input('您要买什么: ').strip()
        if user_choice == '0':
            welcome('')
            print("\n您购买了如下商品: \n" )
            #输入购买的商品
            for i in choice_name_list:
                #print(i.rjust(20))  #本想右对齐,但是输出太不美观
                print(i)
            #计算全部花费
            cost = sum(choice_list)
            print('\n您此次共消费 %s 元.'%cost)
            #开始结算
            #输入支付银行卡卡号和密码
            #判断额度,也就是atm的转账功能
            #一种结算方式,登录商城账号,结合卡号
            raw = input("\n登录后支付（l)\n直接支付 (p)\n\n您的选择：")
            if raw == 'p':
                #支付等于转账
                i = 0
                while i < 3:
                    u_account = input('请输入您的银行卡号: ').strip()
                    u_passwd = input('请输入银行密码: ').strip()
                    if atm.s_login(u_account,u_passwd) is True:
                        msg = '%登录成功!'
                        u_amount = atm.q_amount(u_account)[0]
                        shop_account = '6224407126081192'
                        shop_amount = atm.q_amount(shop_account)[0]
                        new_u_amount = u_amount - cost
                        if new_u_amount >= 0:
                            new_shop_amount = shop_amount + cost
                            atm.up_amount(u_account,new_u_amount)
                            atm.up_amount(shop_account,new_shop_amount)
                            #print('客户当前账户余额%s'%new_u_amount)
                            #print('商城当前账户余额%s'%new_shop_amount)
                            print('\n交易正在处理中,请稍后...')
                            welcome('支付成功')
                            exit()
                    else:
                        print('卡号或者密码错误!请重新输入...')
                        i=i+1
                else:
                    print('尝试次数过多...')
                    exit()
            elif raw == 'l':
                i = 0
                while i < 3:
                    i_name = input('请输入用户名: ').strip()
                    i_passwd = input('请输入密码: ').strip()
                    if handle.active(i_name) is False:
                        time.sleep(0)
                        msg = '%s 该账户已经被锁定,请联系客服工作人员!' % i_name
                        print(msg)
                        #log(i_name,msg)
                        exit()
                    #如果选择登录后支付,判断银行卡号登录
                    elif handle.login(i_name,i_passwd) is True:
                        msg = '%s 登录成功!' % i_name
                        print(msg)
                        #登录成功后,查询用户余额是否大于cost
                        #查询商城银行账户,增加cost
                        u_account = handle.account(i_name)[0]
                        u_amount = atm.q_amount(u_account)[0]
                        shop_account = '6224407126081192'
                        shop_amount = atm.q_amount(shop_account)[0]
                        new_u_amount = u_amount - cost
                        #如果大于则扣款
                        if new_u_amount >= 0:
                            new_shop_amount = shop_amount + cost
                            atm.up_amount(u_account,new_u_amount)
                            atm.up_amount(shop_account,new_shop_amount)
                            #print('客户当前账户余额%s'%new_u_amount)
                            #print('商城当前账户余额%s'%new_shop_amount)
                            print('\n交易正在处理中,请稍后...')
                            welcome('支付成功')
                            exit()
                        else:
                            #否则提示重新输入银行卡号和密码
                            print('余额不足,请更换银行卡...')
                            i = 0
                            while i < 3:
                                u_account = input('请输入您的银行卡号: ').strip()
                                u_passwd = input('请输入银行密码: ').strip()
                                if atm.s_login(u_account,u_passwd) is True:
                                    msg = '%登录成功!'
                                    u_amount = atm.q_amount(u_account)[0]
                                    shop_account = '6224407126081192'
                                    shop_amount = atm.q_amount(shop_account)[0]
                                    new_u_amount = u_amount - cost
                                    if new_u_amount >= 0:
                                        new_shop_amount = shop_amount + cost
                                        atm.up_amount(u_account,new_u_amount)
                                        atm.up_amount(shop_account,new_shop_amount)
                                        #print('客户当前账户余额%s'%new_u_amount)
                                        #print('商城当前账户余额%s'%new_shop_amount)
                                        print('\n交易正在处理中,请稍后...')
                                        welcome('支付成功')
                                        exit()
                                else:
                                    print('卡号或者密码错误!请重新输入...')
                                    i=i+1
                            else:
                                print('尝试次数过多...')
                                exit()
                            exit()
                    else:
                        msg = '%s 账号或者密码错误,请重新输入' % i_name
                        print(msg)
                        #log(i_name,msg)
                        i +=1
                else:
                    time.sleep(0)
                    handle.clock_account(i_name)
                    msg = '\n %s 输入错误次数过多,账号被锁定,请联系客服人员...'% i_name
                    print(msg)
                    #log(i_name,msg)
            else:
                exit()

        elif True:
            #取出商品ID,根据ID判断价格
            id = int(user_choice)
            u_price = handle.select_price(id)
            u_name = handle.select_name(id)
            print('您添加了:%s 价格为: %s'% (u_name,u_price))
            #把价格和商品名称加入list
            choice_list.extend(u_price)
            choice_name_list.extend(u_name)
            continue

        else:
            print('请重新输入')
            exit()




from backend.logic import handle
import random,time,datetime


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
    i_account = str(random.randint(6200000000000000,6299999999999999))
    i_amount = random.randint(0,99999999)
    i_status = 0
    i_date = create_date()
    handle.reg(i_name,i_passwd,i_account,i_amount,i_mail,i_status,i_date)
def nomal():
    while True:
        welcome()
        raw = input('1  额度查询\n2  转账\n3  取款\n4  存款\n5  账单查询\n6  退出\n请输入您要办理的业务: ').strip()
        if raw == '1':
            print('您的额度为:%s\n'%(handle.amount(i_name)))
            continue
        elif raw == '2':
            n = True
            while n:
                transfer_accounts = input('请输入对方银行卡号: ').strip()
                #transfer_amount = int(input('请输入转出金额:   ').strip())
                #transfer_accounts = '6224407126081192'
                #transfer_amount = 100
                #根据卡号取出用户名信息
                to_name = handle.account(transfer_accounts)
                #如果能得到目的用户的用户名那么就执行下一步
                while to_name != False :
                    transfer_amount = int(input('请输入转出金额:   ').strip())
                    #转账分两部分,原用户减钱,目的用户增加钱
                    new_amount_from = handle.amount(i_name) - transfer_amount
                    if new_amount_from  >= 0:
                        new_amount_to = handle.amount(to_name) + transfer_amount
                        handle.update_amount(i_name,new_amount_from)
                        handle.update_amount(to_name,new_amount_to)
                        print('您的当前额度为:%s'%(handle.amount(i_name)))
                        welcome()
                        msg = '%s 转出 %s .' % (i_name,transfer_amount)
                        log(i_name,msg)
                        n = False
                        break
                    else:
                        print('余额不足,请重新输入...')

                else:
                    print('卡号错误,请重新输入...')
        elif raw == '3':
            while True:
                #print('取多少钱')
                raw = int(input('您要取多少: ').strip())
                #raw = 100
                new_amount = handle.amount(i_name) - raw
                if new_amount >= 0:
                    handle.update_amount(i_name,new_amount)
                    print('系统处理中,请稍后...')
                    time.sleep(3)
                    print('您的当前余额为:%s'%handle.amount(i_name))
                    welcome()
                    msg = '%s 取现 %s.'% (i_name,raw)
                    log(i_name,msg)
                    break
                else:
                    print("余额不足,请重新输入!")
        elif raw == '4':
            raw = int(input('您要存多少: ').strip())
            #raw = int(input('我放了100块,你们都看到了啊!!!').strip())
            #raw = random.randint(0,99999999)
            #raw = 100
            print('系统处理中,请稍后...')
            time.sleep(3)
            new_amount = handle.amount(i_name) + raw
            handle.update_amount(i_name,new_amount)
            print('\n您的当前余额为:%s \n'%handle.amount(i_name))
            welcome()
            msg = '%s 存款 %s .' % (i_name,raw)
            log(i_name,msg)
            continue
        elif raw == '5':
            print('您的账单信息:')
            time.sleep(1)
            handle.select_log(i_name)

        else:
            print('即将退出...')
            time.sleep(3)
            exit()
    #break
def admin():
    raw = input('\n欢迎使用ATM后台管理系统\n1  账号查询\n2  账号解锁\n3  账号锁定\n4  账号注销\n5  退出\n请输入您要办理的业务: ').strip()
    if raw == '1':
        print('当前所有账号: \n')
        handle.select_all()
        log('查询当前所有账号')
    elif raw == '2':
        user_choice = input('\n请输入您要解锁的卡号: ').strip()
        status = 0
        handle.update_clock(user_choice,status)
        msg = '%s 已经解除限制.\n'% user_choice
        print(msg)
        log(i_name,msg)
    elif raw == '3':
        user_choice = input('\n请输入您要锁定的卡号: ').strip()
        status = 1
        handle.update_clock(user_choice,status)
        msg = '%s 已经锁定该账号.\n'% user_choice
        print(msg)
        log(i_name,msg)
    elif raw == '4':
        user_choice = input('请输入您要注销的账号: ').strip()
        handle.del_user(user_choice)
        msg = '%s 已经被注销!' % user_choice
        print(msg)
        log(i_name,msg)
    else:
        exit()
def log(name,event):
    date = create_date()
    handle.log(name,date,event)


#欢迎信息
def welcome(hello):
    res = hello.center(100,'*')
    return print(res)
choice_list = []

if __name__ == '__main__':
    welcome("欢迎登录网上商城，祝您购物愉快！")
    #user_choice = input("\n请选择用户登录（l)\n请选择新用户注册 (r)\n\n您的选择：")
    #循环展示商品,用户输入购买选项
    while True:
        handle.select_all()
        user_choice = input('您要买什么: ').strip()
        if user_choice == '0':
            welcome('')
            print("\n您购买了如下商品:\n")
            print('您此次共消费 %s .'%sum(choice_list))
            '''
            for k,v in goods_count().items():
                #print("你要买的商品有 %s,数量为 %s" %(k,v))
                print(k,v)
            '''
            welcome('正在支付中，请稍后')
            time.sleep(0)
            print('\n支付完成\n欢迎下次光临！')

            exit()
        elif True:
            id = int(user_choice)
            u_price= handle.select_price(id)
            print('价格为: %s'% u_price)
            choice_list.extend(u_price)
            continue

        else:
            print('请重新输入')
            exit()




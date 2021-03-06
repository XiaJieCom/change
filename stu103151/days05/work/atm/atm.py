from backend.logic import handle
import random,time,datetime

#欢迎信息
def welcome():
    res = ''.center(100,'#')
    return print(res)
#创建时间
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
#随机生成的邮件地址
def create_mail():
    random_num = random.randint(11111111111,99999999999)
    res =str(random_num)  + '@163.com'
    return res
#时间
def create_date():
    c_date = datetime.datetime.now()
    return c_date
#注册
def reg_user():
    i_name = input('Input your name: ').strip()
    i_passwd = input('Input your passwd: ').strip()
    i_mail = create_mail()
    i_account = str(random.randint(6200000000000000,6299999999999999))
    i_amount = random.randint(0,99999999)
    i_status = 0
    i_date = create_date()
    handle.reg(i_name,i_passwd,i_account,i_amount,i_mail,i_status,i_date)
#普通用户角色的功能
def nomal():
    while True:
        welcome()
        raw = input('1  额度查询\n2  转账\n3  取款\n4  存款\n5  账单查询\n6  退出\n请输入您要办理的业务: ').strip()
        #额度查询
        if raw == '1':
            print('您的额度为:%s\n'%(handle.amount(i_name)))
            #print('您的额度为:%s\n'%(handle.q_amount('6272121765319008')))
            continue
        #转账
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
        #取款
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
        #存款
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
        #操作日志
        elif raw == '5':
            print('您的账单信息:')
            time.sleep(1)
            handle.select_log(i_name)
        #退出
        else:
            print('即将退出...')
            time.sleep(3)
            exit()
    #break
#管理员角色
def admin():
    raw = input('\n欢迎使用ATM后台管理系统\n1  账号查询\n2  账号解锁\n3  账号锁定\n4  账号注销\n5  退出\n请输入您要办理的业务: ').strip()
    #查询所有账户信息
    if raw == '1':
        print('当前所有账号: \n')
        handle.select_all()
        log('查询当前所有账号')
    #解锁
    elif raw == '2':
        choice = input('\n请输入您要解锁的卡号: ').strip()
        status = 0
        handle.update_clock(choice,status)
        msg = '%s 已经解除限制.\n'% choice
        print(msg)
        log(i_name,msg)
    #锁定
    elif raw == '3':
        choice = input('\n请输入您要锁定的卡号: ').strip()
        status = 1
        handle.update_clock(choice,status)
        msg = '%s 已经锁定该账号.\n'% choice
        print(msg)
        log(i_name,msg)
    #注销
    elif raw == '4':
        choice = input('请输入您要注销的账号: ').strip()
        handle.del_user(choice)
        msg = '%s 已经被注销!' % choice
        print(msg)
        log(i_name,msg)
    else:
        exit()
#操作日志函数
def log(name,event):
    date = create_date()
    handle.log(name,date,event)

if __name__ == '__main__':
    raw = input('欢迎使用Automatic Teller Machine系统, 请选择开卡或者登录 (r or l) : ').strip()
    #注册开卡
    if raw == 'r':
        reg_user()
    #邓肯
    elif raw == 'l':
        i = 0
        while i < 3:
            #i_name = 'N485'
            #i_passwd = '123'
            i_name = input('Input your name: ').strip()
            i_passwd = input('Input your passwd: ').strip()
            #print(handle.login(i_name,i_passwd))
            i_amount = random.randint(0,99999999)
            #判断用户状态是否正常,如果不正常则退出
            if handle.active(i_name) is False:
                time.sleep(0)
                msg = '%s 该账户已经被锁定,请联系客服工作人员!' % i_name
                print(msg)
                log(i_name,msg)
                exit()
            #登录验证
            elif handle.login(i_name,i_passwd) is True:
                msg = '%s 登录成功!' % i_name
                print(msg)
                #log(i_name,msg)
                #判断用户角色,根据角色显示不同菜单
                while True:
                    if handle.role(i_name) is True:
                        nomal()
                    else:
                        admin()
            else:
                msg = '%s 账号或者密码错误,请重新输入' % i_name
                print(msg)
                log(i_name,msg)
                i +=1

        else:
            time.sleep(0)
            handle.clock_account(i_name)
            msg = '\n %s 输入错误次数过多,账号被锁定,请联系客服人员...'% i_name
            print(msg)
            log(i_name,msg)
    else:
        exit()

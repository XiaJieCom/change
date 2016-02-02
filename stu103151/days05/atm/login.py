from backend.logic import handle
import random,time


if __name__ == '__main__':
    #handle.home()
    raw = input('欢迎使用Automatic Teller Machine系统, 请选择开卡或者登录 (r or l) : ').strip()
    if raw == 'r':
        #i_name = input('Input your name: ').strip()
        #i_passwd = input('Input your passwd: ').strip()
        #i_name = chr(random.randint(97, 122))
        #i_passwd = str(random.randint(111111,999999))
        i_name = 'shop'
        i_passwd = '123'
        i_mail = '13121889803@163.com'
        i_account = str(random.randint(6200000000000000,6299999999999999))
        i_amount = str(random.randint(0,99999999))
        handle.reg(i_name,i_passwd,i_account,i_mail)
    elif raw == 'l':
        i = 0
        while i < 3:
            #i_name = input('Input your name: ').strip()
            #i_passwd = input('Input your passwd: ').strip()
            #print(handle.login(i_name,i_passwd))
            i_name = 'tom'
            i_passwd = '123'
            i_amount = random.randint(0,99999999)
            if handle.login(i_name,i_passwd) is True:
                print('登录成功!')
                while True:
                    raw = input('1  额度查询\n2  转账\n3  取款\n4  存款\n5  退出\n请输入您要办理的业务: ').strip()
                    if int(raw) == 1:
                        print('您的额度为:%s'%(handle.amount(i_name)))
                        continue
                    elif int(raw) == 2:
                        while True:
                            #transfer_accounts = input('请输入对方银行卡号: ').strip()
                            transfer_amount = int(input('请输入转入金额:   ').strip())
                            transfer_accounts = '6224407126081192'
                            #transfer_amount = 100
                            #根据卡号取出用户名信息
                            to_name = handle.account(transfer_accounts)
                            #转账分两部分,原用户减钱,目的用户增加钱

                            new_amount_from = handle.amount(i_name) - transfer_amount
                            if new_amount_from  > 0:
                                new_amount_to = handle.amount(to_name) + transfer_amount
                                handle.update_amount(i_name,new_amount_from)
                                handle.update_amount(to_name,new_amount_to)
                                print('您的额度为:%s'%(handle.amount(i_name)))
                                break
                            else:
                                print('余额不足,请重新输入...')

                    elif int(raw) == 3:
                        #print('取多少钱')
                        raw = int(input('您要取多少: ').strip())
                        #raw = 100
                        new_amount = handle.amount(i_name) - raw
                        handle.update_amount(i_name,new_amount)
                        print('系统处理中,请稍后...')
                        time.sleep(3)
                        print('余额为:%s'%handle.amount(i_name))
                        continue
                    elif int(raw) == 4:
                        raw = int(input('您要存多少: ').strip())
                        #raw = int(input('我放了100块,你们都看到了啊!!!').strip())
                        #raw = random.randint(0,99999999)
                        #raw = 100
                        print('系统处理中,请稍后...')
                        time.sleep(3)
                        new_amount = handle.amount(i_name) + raw
                        handle.update_amount(i_name,new_amount)
                        print('余额为:%s'%handle.amount(i_name))
                        exit()




















                break
            else:
                print('账号或者密码错误,请重新输入')
                i +=1

        else:
            time.sleep(3)
            print('\n输入错误次数过多,账号被锁定,请联系客服人员.')
    else:
        exit()

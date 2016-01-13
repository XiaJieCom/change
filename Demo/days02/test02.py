__author__ = 'jack'
#判断用户名密码是否正确
def login(name,passwd):
    with open('passwd.txt') as f:
        if (name + ':'+ passwd) in f.read():
            return True
        else:
            print("Invalid user ...")
            return False
#将错误用户加入黑名单
def black_list(name):
    print("Too many times to try again...")
    with open('stop.txt','a+') as stop:
        stop.write(i_name + '\n' )
    return
#判断用户是否在黑名单里
def back_in(name):
    with open('stop.txt') as stop:
        if name in stop.read():
            print("Your are in blacklist...")
            return False
#注册功能
def reg(name,passwd,amount):
    print("Your name is %s, and passwd is %s."%(name,passwd))
    with open('passwd.txt','a+') as f:
        f.write(name + ':' + passwd +'$'+ amount + '\n' )
    return True
#将选购的商品加入shopping_dict
def goods_count():
    shoppping_dict = {}
    for i in choice_list:
        #将出现的商品名称作为key,出现的次数作为value 写入shopping_dict
        shoppping_dict[i[0]] = choice_list.count(i)
    return shoppping_dict


choice_list = []
product_list = [
    #('退出',0),
    ('iPhone 7          ',5800),
    ('iPhone 6s         ',4000),
    ('Smartisan T1      ',1999),
    ('Smartisan T12     ',2999),
    ('Coffee            ',35),
    ('XiaoMi 2s         ',350),
    ('MX 4              ',1999),
    ('Mac mini          ',6600),
    ('Macbook pro       ',10000),
]
print("欢迎登录网上商城，祝您购物愉快！")
while True:
    #输入选择，注册，登录，或者退出
    choice = input("\n请选择老用户登录（l)\n请选择新用户注册 (r)\n您的选择：")
    if choice == 'r':
        i_name = input("请输入用户名:").strip()
        i_passwd = input("请输入密码:").strip()
        i_amount = input("请输入您的授权额度:").strip()
        reg(i_name,i_passwd,i_amount)
        continue
    elif choice == 'l':
        c = 0
        print(type(c))
        while c <3:
            i_name = input("input your name:").strip()
            i_passwd = input("input your passwd:").strip()
            if back_in(i_name) == False:
                exit()
            else:
                if login(i_name,i_passwd) == True:
                    while True:
                        #with open('passwd.txt') as f:

                        amount = int(input("please input your amount: ").strip())
                        if amount <= 0:
                            print("输入有误，请重新输入")
                            continue
                        else:
                            break
                        
                    while True:
                        index = 1
                        for i in product_list:
                            print(index,i[0],i[1])
                            index += 1
                        user_choice = int(input("你要买什么: ").strip())
                        if user_choice == 0:
                            print("\n您购买了如下商品:\n")
                            for k,v in goods_count().items():
                                #print("你要买的商品有 %s,数量为 %s" %(k,v))
                                print(k,v)
                            exit()
                        elif user_choice <= len(product_list):
                            print(len(product_list))
                            user_choice -= 1
                            item_price = product_list[user_choice][1]
                            if amount >= item_price:
                                amount -= item_price
                                choice_list.append(product_list[user_choice])
                                print( "You have \033[31;1m%d\033[0m left!" % amount)
                            else:
                                print( "You have \033[31;1m%d\033[0m left!" % amount)
                                print("您的余额不足，请尝试购买其他商品!")
                                continue
                        else:
                            print('请重新输入')
                else:
                    print("用户名或者密码错误")
                    c += 1
        else:
            black_list(i_name)
            exit()
    else:
        print("欢迎下次光临!")
        exit()

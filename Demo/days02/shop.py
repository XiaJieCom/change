__author__ = 'jack'
"""
shopping_dict = {
    "酒":{
        '啤酒':[('黑啤酒',10),('扎啤',5),('白啤',15)],
        '红酒':[(82,10000),(90,5000),(100,500),],
        '白酒':[('茅台',500),('五粮液',600),('海之蓝',200)]
        },
    "饮料":{
        '可乐':[('百事可乐',3.5),('可口可乐',3.5),('非常可乐'),'3.5'],
        'tea':[('lv tea',10),('hong tea',8),('普洱',20)],
        '水':[('哇哈哈',3),('农夫山泉',2),('康师傅',2.5)]
    },
    "手机":{
        '智能机':[('T1',2999),('iPhone',4800),('MX 4',1999),],
        '平价机':[('红米',799),('坚果',699),('note',599)],
        '功能机':[('金立',100),('诺基亚 101',200),('三星',150)]
    }
}
"""
choice_list = []
product_list = [
    #('退出',0),
    ('iPhone      ',5800),
    ('Bike        ',800),
    ('Book        ',45),
    ('Coffee      ',35),
    ('Solo 2 Beats',1590),
    ('MX4         ',1999),
]
print("欢迎登录网上商城，祝您购物愉快！")
while True:
    #输入选择，注册，登录，或者退出
    choice = input("\n请选择老用户登录（l)\n请选择新用户注册 (r)\n您的选择：")
    #如果选择注册，以i_name:i_passwd的格式存入passwd.txt文件中
    if choice == 'r':
        i_name = input("Please input your name: ").strip()
        i_passwd = input("Please input your passwd: ").strip()
        print("Your name is %s, and passwd is %s."%(i_name,i_passwd))
        with open('passwd.txt','a+') as f:
            f.write(i_name + ':' + i_passwd + '\n' )
    #如果选择登录
    elif choice == 'l':
        i = 0
        while i < 3:
            i_name = input("Please input your name: ").strip()
            i_passwd = input("Please input your passwd: ").strip()
            #先检查是否存在黑名单stop.txt中，如果存在就退出；否则就尝试登录
            with open('stop.txt','a+') as stop:
                if i_name in stop.read():
                    print("Your are in blacklist...")
                    exit()
                else :
                    with open('passwd.txt') as f:
                        if (i_name + ':'+ i_passwd) in f.read():
                            print("登录成功！")
                            #####下面是购物车功能
                            while True:
                                salary = int(input("please input your salary: ").strip())
                                if salary <= 0:
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
                                    #print(choice_list)
                                    shoppping_dict = {}
                                    for i in choice_list:
                                        #将出现的商品名称作为key,出现的次数作为value 写入shopping_dict
                                        shoppping_dict[i[0]] = choice_list.count(i)
                                    #print(a)
                                    #打印shopping_dict
                                    print("\n您购买了如下商品:\n")
                                    for k,v in shoppping_dict.items():
                                        #print("你要买的商品有 %s,数量为 %s" %(k,v))
                                        print(k,v)
                                    break
                                elif user_choice <= len(product_list):
                                    print(len(product_list))
                                    user_choice -= 1
                                    item_price = product_list[user_choice][1]
                                    if salary >= item_price:
                                        salary -= item_price
                                        choice_list.append(product_list[user_choice])
                                        print( "You have \033[31;1m%d\033[0m left!" % salary)
                                    else:
                                        print( "You have \033[31;1m%d\033[0m left!" % salary)
                                        print("您的余额不足，请尝试购买其他商品!")
                                        continue
                                else:
                                    print('请重新输入')
                            #购物车结束
                        else:
                            print("Invalid user ...")
                            i += 1
                            #如果输错一次，i自增
        #如果错误三次，就加入黑名单，并强制退出
        else:
            print("Too many times to try again...")
            with open('stop.txt','a+') as stop:
                stop.write(i_name + '\n' )
            exit()
    #如果不选择注册、登录，就退出
    else:
        print("欢迎下次光临！")
        exit()

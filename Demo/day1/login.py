#/usr/bin/env python3
#__author__ = 'jack'


'''
if choice == 'login':
    i_name = input("Plases input your name: ").strip()
    i_pass = input("Please input your passwd: ").strip()
elif choice == 'registry':
    with open('passwd.txt','a') as f:
        r_name = input("Please input you want name: ").strip()
        r_pass = input("Please input you want passwd:").strip()
        f.write(r_name)
        f.writable(":")
        f.write(r_pass,"\n")
        print("Sucessful!")
else:
    exit
    '''

'''
choice_list = ['login','registry','quit']
for i in choice_list:
    print(choice_list.index(i),i)
    '''
"""
name = 'tom'
passwd = 'cat'

#choice = input("Please input your choice: ").strip()
i = 0
while i < 3:
    i_name = input("Please input your name: ").strip()
    i_passwd = input("Please input your name: ").strip()


    if i_name == name and i_passwd == passwd:
        print("welcome my world!")
        break
    else:
        print("Invalid user...")
        i += 1

else:
    print("Too many times to try again...")

"""


'''
#定义函数，负责输入账号和密码
while True:
    choice = input("Please input your choice, regstry or login (r/l/q)? ")
    if choice == 'r':
        #如果选择注册，就写入passd.txt文件
        input_info()
        print("Your name is %s, and passwd is %s."%(i_name,i_passwd))
        with open('passwd.txt','a+') as f:
            f.write(i_name + ':' + i_passwd + '\n' )
    elif choice == 'l':
        #否则就是登录，判断用户名密码是否匹配，3次退出
        i = 0
        while i < 3:
            input_info()
            f = open('passwd.txt').read()
            if f.find(i_name +':'+ i_passwd) !=-1:
                print("welcome my world!")
                exit()
            else:
                print("Invalid user...")
                i += 1
        else:
            print("Too many times to try again...")
            print("You must stop, %s!"% i_name)
            with open('stop.txt','a+') as f:
                f.write(i_name + '\n' )
                time.sleep(10)
    else:
        print("You can go out!!!")
        exit()

'''

import time
def input_info():
    global i_name
    i_name = input("Please input your name: ").strip()
    global i_passwd
    i_passwd = input("Please input your passwd: ").strip()
def registry():
    input_info()
    print("Your name is %s, and passwd is %s."%(i_name,i_passwd))
    with open('passwd.txt','a+') as f:
        f.write(i_name + ':' + i_passwd + '\n' )
def login():
    i = 0
    while i < 3:
        input_info()
        f = open('passwd.txt').read()
        stop = open('stop.txt').read()
        if f.find(i_name +':'+ i_passwd) !=-1 and stop.find(i_name) == -1:
            print("welcome my world!")
            exit()
        else:
            print("Invalid user...")
            i += 1
    else:
        print("Too many times to try again...")
        print("You must stop, %s!"% i_name)
        with open('stop.txt','a+') as f:
            f.write(i_name + '\n' )
            print("You have been added to the black list.\n3 seconds after the withdrawal system!")
            time.sleep(3)
            exit()


while True:
    choice = input("Please input your choice, regstry or login (r/l/q)? ")
    if choice == 'r':
        registry()
    elif choice == 'l':
        login()
    else:
        print("You can go out!!!")
        exit()

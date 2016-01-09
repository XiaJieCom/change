#/usr/bin/env python3
while True:
    #输入选择，注册，登录，或者退出
    choice = input("Please input your choice, registry or login ?  (r/l/q) ")
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
            with open('stop.txt') as stop:
                if i_name in stop.read():
                    print("Your are in blacklist...")
                    exit()
                else :
                    with open('passwd.txt') as f:
                        if (i_name + ':'+ i_passwd) in f.read():
                            print("ok !!!")
                            exit()
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
        print("You can go out!!!")
        exit()
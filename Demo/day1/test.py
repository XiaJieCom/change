#__author__ = 'jack'

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

while True:
    choice = input("Input your choice registry or login ? (r/l) ")
    if choice == 'r':
        registry()
    elif choice == 'l':
        with open('stop.txt') as stop:
            data = stop.read()
            if data.find(i_name) != -1:
                print('stop !!!')
                exit()
            else:
                i = 0
                while i < 3:
                    input_info()
                    f = open('passwd.txt').read()
                    if f.find(i_name +':'+ i_passwd) !=-1:
                        print(f.find(i_name +':'+ i_passwd))
                        print("welcome my world!")
                        exit()
                    else:
                        print("Invalid user...")
                        i += 1
                else:
                    print("Too many times to try again...")
                    with open('stop.txt','a+') as f:
                        f.write(i_name + '\n' )
                        print("I will kill you %s !!!"% i_name)
    else:
        print("Go out !!!")
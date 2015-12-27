#/usr/bin/env python3
#__author__ = 'jack'

choice = input("Please input your choice: ").strip()
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
choice_list = ['login','registry','quit']
for i in choice_list:
    print(choice_list.index(i),i)
    '''
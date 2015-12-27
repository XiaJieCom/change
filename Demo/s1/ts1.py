#!/usr/bin/env python3
'''
with open('passwd.txt','r') as f:
    print(f.read())

'''

with open('passwd.txt','w+') as f:
    f.write('zoo')
    for line in f.readlines():
        print(line)























'''
with open('passwd.txt') as f:
    print(f.read())
'''

'''
file = open('passwd.txt','r')
try:
    data = file.read()
    print(data)
finally:
    file.close()
    print(file.closed)
'''
'''
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print('当前水果 :', fruits[index])

print("Good bye!")
'''

'''
for i in range(10):
    print(i)
'''


'''
print("hahah")
'''
'''
name = input("Please input your name: ")
print(name)
'''
'''
name = input("Please input your name:   ")
job = input("Please input your job: ")
if job == 'cat':
    print("You are Tomcat!")
elif job == 'dog':
    print("Your are dog.")
else:
    print("I don't know ...")
'''
'''
luckey_num = 6

while True:
    choice = int(input("Please input you want :"))
    if choice == luckey_num:
        print("Bingo!!!")
        break
    elif choice > luckey_num:
        print("Too bigger!!!")
    else:
        print("Too smaller!!!")

'''
'''
i = 0
while i<3:
    print(i)
    i += 1
'''
'''
luckey_nm = 6
choice = 0
while luckey_nm != choice:
    choice = int(input("Please input you want :"))
    #if choice == luckey_nm:
    #    print("Bingo!!!")
    #    break
    if choice > luckey_nm:
        print("Too big!!!")
    elif choice < luckey_nm:
        print("Too small!!!")
print("Bingo")
'''
'''
luckey_nm = 6
i = 0
while i < 3:
    choice = int(input("Please input you want :"))
    if choice > luckey_nm:
        print("Too bigger...")
    elif choice < luckey_nm:
        print("Too smaller...")
    else:
        print("Bingo!")
        break
    i += 1
else:
    print("Too many request...")
'''
'''
luckey_nm = 6


for i in range(3):
    choice = int(input("Please input you want :"))
    if choice > luckey_nm:
        print("Too bigger...")
    elif choice < luckey_nm:
        print("Too smaller...")
    else:
        print("Bingo!")
        break

else:
    print("Too many request...")
'''
"""
name = input("Please input your name: ")
age = input("Please input your age: ")
job = input("Plase input your job: ")

msg = '''
Name: %s
Age: %s
Job: %s
'''%(name,age,job)
print(msg)

'''
"""
'''
name_list = ['cat','dog','cat','fish','pig']
for i in range(name_list.count('cat')):
    name_list.remove('cat')
print(name_list)
name_list.extend()
'''

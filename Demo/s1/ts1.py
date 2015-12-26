#!/usr/bin/env python3
#__author__ = 'jack'
'''
print("hahah")
'''
'''
luckey_nm = 6

while True:
    choice = int(input("Please input you want :"))
    if choice == luckey_nm:
        print("Bingo!!!")
        break
    elif choice > luckey_nm:
        print("Too big!!!")
    else:
        print("Too small!!!")

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
luckey_nm = 6
choice = 0
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
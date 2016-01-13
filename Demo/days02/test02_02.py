__author__ = 'jack'
i_name = 'tom'
with open('passwd.txt') as f:
    if (i_name) in f.read():
        print(f.read())

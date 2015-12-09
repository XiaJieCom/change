#!/usr/bin/env pyhon
i = 0
f = file('./admin.txt').read()
while i<3:
	i_name = raw_input("please input your name:")
	i_passwd = raw_input("please input your passwd:")
	if f.find(i_name +':'+ i_passwd) !=-1:
		print "welcome to this to world!!!"
		break
	else:
		print "Sorry, your account number or password input error"
		i +=1

#!/usr/bin/env python
import socket,os
#设定服务器地址和端口
ip_port = ('127.0.0.1',9999)
sk = socket.socket()
#建立连接
sk.connect(ip_port)

#循环执行
while True:
    #用户输入文件名
    user_input = input("The file path:").strip()
    #如果输入为空,那么就回车继续输入
    if len(user_input) == 0:continue
    #如果输入为q就退出
    if user_input == 'q':break
    #cmd,path = user_input.split('|')
    #如果文件不存在就跳出
    if os.path.exists(user_input) == False:
        print('文件或目录不存在!')
        break
    #取出文件名
    f_name = os.path.basename(user_input)


    #取出文件大小
    f_size = os.stat(user_input).st_size
    #发送文件名和大小
    msg = 'name :%s    size:%s '% (f_name,str(f_size))
    sk.send(bytes(msg,'utf8'))
    print(msg)

sk.close()


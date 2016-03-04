#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import socket
ip_port = ('127.0.0.1',9999)
#ip_port = ('114.215.155.140',9999)

sk = socket.socket()
sk.connect(ip_port)

sk.sendall(bytes('This is clinet','utf-8'))
server_replay = sk.recv(1024)
print(str(server_replay,'utf-8'))
while True:
    client_raw = input('>> ').strip()
    sk.sendall(bytes(client_raw,'utf-8'))
    server_replay = sk.recv(1024)
    print('server:',str(server_replay,'utf8'))
sk.close()

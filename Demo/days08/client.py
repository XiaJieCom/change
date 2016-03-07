#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket


ip_port = ('127.0.0.1',9090)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)

while True:
    data = sk.recv(1024)
    print(str(data,'utf-8'))
    inp = input('please input:')
    sk.sendall(bytes(inp,'utf8'))
    if inp == 'exit':
        break

sk.close()


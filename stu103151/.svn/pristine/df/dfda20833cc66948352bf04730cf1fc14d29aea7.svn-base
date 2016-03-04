import socket
#监听地址和端口
ip_port = ('0.0.0.0',9999)
sk  = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print('Server is waiting ... ')
    while True:
        #建立连接
        conn,addr = sk.accept()
        #接收客户端传输的数据
        client_data = conn.recv(1024)
        #如果接收信息为空,就跳出
        if not client_data:break
        #打印信息
        print(str(client_data,'utf-8'))
        #conn.sendall(bytes('这是 server !','utf-8'))
        #再次循环,打印信息

sk.close()
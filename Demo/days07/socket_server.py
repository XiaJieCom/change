import socket
ip_port = ('0.0.0.0',9999)
#ip_port = ('127.0.0.1',9998)
sk  = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print('Server is waiting ... ')
    conn,addr = sk.accept()
    client_data = conn.recv(1024)
    print(str(client_data,'utf-8'))
    #conn.sendall(bytes('这是 server !','utf-8'))
    while True:
        client_data = conn.recv(1024)
        print('client:',str(client_data,'utf8'))
        server_raw = input('>> ').strip()
        if not (client_data):break
        conn.sendall(bytes(server_raw,'utf-8'))
        client_data = conn.recv(1024)
        print(str(client_data,'utf8'))
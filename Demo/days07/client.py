import socket
ip_port = ('127.0.0.1',9090)
#ip_port = ('10.0.6.151',9999)

sk = socket.socket()
sk.connect(ip_port)

sk.sendall(bytes('这是 client !','utf-8'))

server_replay = sk.recv(1024)
print(str(server_replay,'utf-8'))
while True:

    client_raw = input(':').strip()
    sk.sendall(bytes(client_raw,'utf-8'))
    server_replay = sk.recv(1024)
    print(str(server_replay,'utf-8'))



sk.close()
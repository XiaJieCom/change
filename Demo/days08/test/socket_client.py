import socket
ip_port = ('127.0.0.1',8080)
sk = socket.socket()
sk.connect(ip_port)

while True:
    raw = input('>> ').strip()
    sk.send(bytes(raw,'utf8'))
    msg = sk.recv(1024)
    print(str(msg,'utf8'))
sk.close()
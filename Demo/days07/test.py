import socket
ip_port = ('0.0.0.0',9999)
#ip_port = ('127.0.0.1',9998)
sk  = socket.socket()
sk.bind(ip_port)
sk.listen(5)

class Server(object):

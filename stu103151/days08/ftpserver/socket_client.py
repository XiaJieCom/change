import socket,os
'''
ip_port = ('127.0.0.1',8080)
sk = socket.socket()
sk.connect(ip_port)

while True:
    msg = sk.recv(1024)
    print(str(msg,'utf8'))
    while True:
        raw = input('>> ').strip()
        sk.send(bytes(raw,'utf8'))
        msg = sk.recv(1024)
        print(str(msg,'utf8'))
sk.close()
'''
class FTPClient(object):
    def __init__(self,host,port):
        self.sk = socket.socket()
        self.sk.connect((host,port))
        msg = self.sk.recv(1024)
        print(str(msg.decode()))
    def start(self):
        self.active()
    def active(self):
        while True:
            raw = input('>> ').strip()
            if len(raw) == 0:continue
            raw = raw.split()
            if hasattr(self,raw[0]):
                func = getattr(self,raw[0])
                func(raw)
            else:
                print('Wrong cmd usage!')
    def get(self,msg):
        print('---get func---',msg)
        exit()
    def put(self,msg):
        print('---put func---',msg)
        exit()
    def dir(self,msg):
        print('---dir func---',msg)
        exit()
if __name__ == '__main__':
    f = FTPClient('127.0.0.1',8080)
    f.start()
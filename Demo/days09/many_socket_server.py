import sys
import socket
import time
import gevent

from gevent import socket,monkey
monkey.patch_all()
def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(2)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)
def handle_request(s):
    try:
        while True:
            data = s.recv(1024)
            print("recv:", str(data,'utf8'))
            s.send(data)
            if not data:
                s.shutdown(socket.SHUT_WR)

    except Exception as  ex:
        print(ex)
    finally:

        s.close()
if __name__ == '__main__':
    server(8000)
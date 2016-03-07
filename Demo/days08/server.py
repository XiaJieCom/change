import socketserver

class Server(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall(bytes('欢迎致电...','utf8'))
        Flag = True
        while Flag:
            data = conn.recv(1024)
            msg = str(data,'utf8')
            print(type(msg))
            print(msg)

            if msg == 'exit':
                Flag = False
            elif msg == '0':
                conn.sendall(bytes('hahaha...','utf8'))
            else:
                conn.sendall(bytes('重新输入...','utf8'))
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9090),Server)
    server.serve_forever()
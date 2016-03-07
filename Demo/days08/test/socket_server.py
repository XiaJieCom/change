import socketserver

class Server(socketserver.BaseRequestHandler):
    def handle(self):
        print('New connection:',self.client_address)
        while True:
            data = self.request.recv(1024)
            if not data:break
            print('Client data:',data.decode())
            self.request.send(data)

if __name__ == '__main__':
    host,port = '127.0.0.1',8080
    server = socketserver.ThreadingTCPServer((host,port),Server)
    server.serve_forever()

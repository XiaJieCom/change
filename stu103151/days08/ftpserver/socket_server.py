import socketserver

class Server(socketserver.BaseRequestHandler):
    def handle(self):
        print('New connection:',self.client_address)
        self.request.send(str(self.client_address).encode())

        while True:
            client_data = self.request.recv(1024)
            if not client_data:break
            print('Client data:',client_data.decode())
            cmd = str(client_data.decode).strip()
            self.request.send(client_data)

if __name__ == '__main__':
    host,port = '127.0.0.1',8080
    server = socketserver.ThreadingTCPServer((host,port),Server)
    server.serve_forever()

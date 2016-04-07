from twisted.internet import reactor,protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("hello a ")
    def dataReceived(self, data):
        print('Server said:',data)
        self.transport.loseConnection()
    def connectionLost(self, reason):
        print('connection lost')
class EchoFatoty(protocol.ClientFactory):
    protocol = EchoClient
    def clientConnectionFailed(self, connector, reason):
        print('Connection lost - goodbye!')
        reactor.stop()
def main():
    f = EchoFatoty()
    reactor.connectTCP('localhost',9090,f)
    reactor.run()
if __name__ == '__main__':
    main()
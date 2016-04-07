from twisted.internet import protocol
from twisted.internet import reactor

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)
def main():
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(9090,factory)
    reactor.run()
if __name__ == '__main__':
    main()
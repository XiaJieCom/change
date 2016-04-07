from twisted.internet import protocol
from twisted.internet import reactor

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

def main():
    factory = protocol.ServerFactory()
    #定义一个factory
    factory.protocol = Echo
    #定义protocol,Echo
    reactor.listenTCP(1234,factory)
    #监听1234端口
    reactor.run()
    #启动
if __name__ == '__main__':
    main()
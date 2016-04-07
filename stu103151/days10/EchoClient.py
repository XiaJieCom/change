from twisted.internet import reactor, protocol


# a client protocol

class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""

    def connectionMade(self):
        self.transport.write("hello alex!")

    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print("Server said:", data)
        self.transport.loseConnection()

    def connectionLost(self, reason):
        print( "connection lost")

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        '''
        连接错误,提示信息,然后停止
        :param connector:
        :param reason:
        :return:
        '''
        print ("Connection failed - goodbye!")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        '''
        连接断开,提示信息,停止
        :param connector:
        :param reason:
        :return:
        '''
        print ("Connection lost - goodbye!")
        reactor.stop()


# this connects the protocol to a server running on port 8000
def main():
    f = EchoFactory()
    #实例化EchoFactory
    reactor.connectTCP("localhost", 1234, f)
    #连接指定地址信息
    reactor.run()
    #启动
# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
    #开始执行
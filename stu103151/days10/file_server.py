#_*_coding:utf-8_*_
# This is the Twisted Fast Poetry Server, version 1.0

import optparse, os
#optparse 模块用来为脚本传递命令参数功能

from twisted.internet.protocol import ServerFactory, Protocol


def parse_args():
    usage = """usage: %prog [options] poetry-file

This is the Fast Poetry Server, Twisted edition.
Run it like this:

  python fastpoetry.py <path-to-poetry-file>

If you are in the base directory of the twisted-intro package,
you could run it like this:

  python twisted-server-1/fastpoetry.py poetry/ecstasy.txt

to serve up John Donne's Ecstasy, which I know you want to do.
"""

    parser = optparse.OptionParser(usage)
    #创建实例

    help = "The port to listen on. Default to a random available port."
    #help信息
    parser.add_option('--port', type='int', help=help)
    #添加选项.当命令输入出现'--port'时就会被识别,数据类型为'int'

    help = "The interface to listen on. Default is localhost."
    parser.add_option('--iface', help=help, default='localhost')
    #添加选项.如果不指定type参数,默认的是string;
    options, args = parser.parse_args()
    #调用parse_args()获取定义的选项和参数
    print("--arg:",options,args)
    #答应获取的选项和参数
    if len(args) != 1:
        #如果args长度不为1,说明格式错误
        parser.error('Provide exactly one poetry file.')

    poetry_file = args[0]
    #文件名称
    if not os.path.exists(args[0]):
        #如果文件不存在,提示错误信息
        parser.error('No such file: %s' % poetry_file)

    return options, poetry_file
    #返回选项和文件名

class PoetryProtocol(Protocol):

    def connectionMade(self):
        self.transport.write(self.factory.poem)
        self.transport.loseConnection()


class PoetryFactory(ServerFactory):

    protocol = PoetryProtocol

    def __init__(self, poem):
        self.poem = poem


def main():
    options, poetry_file = parse_args()

    poem = open(poetry_file).read()
    #读取poetry_file
    factory = PoetryFactory(poem)

    from twisted.internet import reactor

    port = reactor.listenTCP(options.port or 9000, factory,
                             interface=options.iface)

    print('Serving %s on %s.' % (poetry_file, port.getHost()))

    reactor.run()


if __name__ == '__main__':
    main()
    #从main()开始执行
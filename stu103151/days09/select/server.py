#_*_coding:utf-8_*_

import select
import socket
import sys
import queue

# 生成 socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)

# 监听地址和端口
server_address = ('localhost', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
server.bind(server_address)

# 监听数量最大值
server.listen(5)

# Sockets from which we expect to read
#读取server端输入信息
inputs = [ server ]

# Sockets to which we expect to write
#输出信息
outputs = [ ]

message_queues = {}
#信息的队列
while inputs:

    # Wait for at least one of the sockets to be ready for processing
    #进入阻塞状态,等待接收
    print( '\nwaiting for the next event')
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    # Handle inputs
    for s in readable:

        if s is server:
            # A "readable" server socket is ready to accept a connection
            connection, client_address = s.accept()
            #连接一个客户端
            print('new connection from', client_address)
            #打印客户端的地址
            connection.setblocking(False)
            #False设置socket为非阻塞模式.在非阻塞模式下, 如果recv()调用没有发现任何数据或者send()调用无法立即发送数据, 那么将引发socket.error异常。在阻塞模式下, 这些调用在处理之前都将被阻塞。
            inputs.append(connection)
            #将socket连接加入inputs

            # Give the connection a queue for data we want to send
            message_queues[connection] = queue.Queue()
            #将连接要发送的数据加入队列
        else:
            data = s.recv(1024)
            #设置默认接收1024字节的数据
            if data:
                #如果data不为空
                # A readable client socket has data
                print(sys.stderr, 'received "%s" from %s' % (data, s.getpeername()) )
                message_queues[s].put(data)
                #取出序列里的数据
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
            else:
                #否则说明数据为空,说明要断开连接
                # Interpret empty result as closed connection
                print('closing', client_address, 'after reading no data')
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)  #既然客户端都断开了，我就不用再给它返回数据了，所以这时候如果这个客户端的连接对象还在outputs列表中，就把它删掉
                inputs.remove(s)    #inputs中也删除掉
                s.close()           #把这个连接关闭掉

                # Remove message queue
                del message_queues[s]
                #删除该序列
    # Handle outputs
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
            #相当Queue.get(False)
        except queue.Empty:
            # No messages waiting so stop checking for writability.
            print('output queue for', s.getpeername(), 'is empty')
            outputs.remove(s)
        else:
            print( 'sending "%s" to %s' % (next_msg, s.getpeername()))
            s.send(next_msg)
    # Handle "exceptional conditions"
    for s in exceptional:
        print('handling exceptional condition for', s.getpeername() )
        # Stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        # Remove message queue
        del message_queues[s]
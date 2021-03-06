import socket,os,sys,time

class FTPClient(object):
    '''
    定义FTPClient类
    '''
    def __init__(self,host,port):
        self.sk = socket.socket()
        self.sk.connect((host,port))
        #初始化连接
        #msg = self.sk.recv(1024)
        #print(str(msg.decode()))
    def start(self):
        self.active()
        #开始执行,active()
    def active(self):
        while True:
            raw = input('>> ').strip()
            if len(raw) == 0:continue
            raw = raw.split()
            #输入指令,判断是上传还是下载
            if hasattr(self,raw[0]):
                func = getattr(self,raw[0])
                func(raw)
            else:
                print('Wrong cmd usage!')
    def get(self,cmd):
        #如果是下载
        print('---get func---',cmd)
        if len(cmd) == 2:
            print("That's ok!")
            #取出文件名cmd[1]
            f_name = cmd[1]
            transfer = 'transfer|get|%s' % f_name
            self.sk.send(bytes(transfer,'utf8'))
            #将文件信息传给服务端
            feed_back = str(self.sk.recv(1024).decode())
            print('-->',feed_back)
            if feed_back.startswith('transfer|get|ready'):
                f_size = int(feed_back.split("|")[-1])
                #接收服务端返回信息,输出文件大小
                print(f_size)
                self.sk.send(bytes('transfer|get|recv_ready'.encode()))
                #客户端返回信息,提示服务端可以传输
                recv_size = 0
                #下载后的存放路径和文件名
                new_file = '%s/%s'%('/tmp/client',os.path.basename(f_name))
                with open (new_file,'wb') as f:
                    #print('-->',f_name)
                    while not f_size == recv_size:
                        if f_size - recv_size > 1024:
                            data = self.sk.recv(1024)
                            recv_size += len(data)
                        else:
                            data = self.sk.recv(f_size - recv_size)
                            recv_size += (f_size - recv_size)
                        f.write(data)
                        #rep(f_size,recv_size)
                        tmp = recv_size/f_size
                        print(format(tmp,'.4%'))
                    else:
                        print('---recv file:%s---'% f_name)
        else:
            print('Wrong cmd usage!')
            exit()
    def put(self,cmd):
        if cmd[0] == 'put':
            print("That's ok!")
            f_name = cmd[1]
            transfer = 'transfer|put|%s' % f_name
            self.sk.send(bytes(transfer,'utf8'))
            feed_back = str(self.sk.recv(1024).decode())
            print('-->',feed_back)
            if feed_back.startswith('transfer|put|ready'):
                f_size = int(feed_back.split("|")[-1])
                self.sk.send(bytes('transfer|put|recv_ready'.encode()))
                print(f_size)
                recv_size = 0
                new_file = '%s/%s'%('/tmp/server',os.path.basename(f_name))
                with open (new_file,'wb') as f:
                    #写入新文件到指定路径
                    print('-->',f_name)
                    time.sleep(0.1)
                    while not f_size == recv_size:
                        if f_size - recv_size > 1024:
                            data = self.sk.recv(1024)
                            recv_size += len(data)
                            #进度条
                            bar_length=100
                            for percent in range(0,101):
                                hashes = '#' * int(recv_size/f_size  * bar_length)
                                spaces = ' ' * (bar_length - len(hashes))
                                sys.stdout.write("\rPercent: [%s] %d%%"%(hashes + spaces, percent))
                                sys.stdout.flush()
                                #time.sleep(0.1)
                        else:
                            data = self.sk.recv(f_size - recv_size)
                            recv_size += (f_size - recv_size)

                        f.write(data)
                        #print(f_size,recv_size)
                        tmp = recv_size / f_size
                        #print('已完成',format(tmp,'.4%'),)
                    else:
                        print('\n---recv file:%s---'% f_name)

    def exit(self,cmd):
        raw = input('你真的要退出吗? y/n ').strip()
        if raw == 'y':
            exit()
    def help(self,cmd):
        print('---欢迎使用FTP客户端---'
          '\nget filename',
          '\nput filename'
          '\nexit'
          '\nhelp\n'
          )
if __name__ == '__main__':
    print('---欢迎使用FTP客户端---'
          '\nget filename',
          '\nput filename'
          '\nexit'
          '\nhelp\n'
          )
    f = FTPClient('127.0.0.1',8082)
    f.start()

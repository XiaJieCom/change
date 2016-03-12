import threading,time,paramiko,os
from configparser import ConfigParser

#读取配置文件
config = ConfigParser()
config.read('config.ini')
#获取主机IP
hostname = ''.join(config.get('IP','ip'))
#对主机IP进行';'切割
address = hostname.split(';')
print(address)

#取出username和passwd
username = ''.join(config.get('Name','username'))
passwd = ''.join(config.get('Passwd','passwd'))

#上传下载路径
src_dir = '/tmp/test.txt'
des_dir = '/tmp/test.txt'
#命令执行函数
def cmd():
    '''
    执行远程命令
    :return:
    '''
    #取出IP
    for ip in address:
        #记录到日志
        paramiko.util.log_to_file('paramiko.log')
        #连接一台主机
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #根据之前取到的IP等信息
        s.connect(hostname=ip,port =22,username=username,password=passwd)
        #输出命令执行结果
        stdin,stdout,stderr=s.exec_command('df -h ')
        print (stdout.read() )
        s.close()

def send():
    '''
    文件上传
    :return:
    '''
    #循环IP
    for ip in address:
        #打印日志
        paramiko.util.log_to_file('paramiko-send.log')
        #根据取到的IP等信息建立连接
        t=paramiko.Transport((ip,22))
        t.connect(username=username,password=passwd)
        #传输文件
        sftp=paramiko.SFTPClient.from_transport(t)
        sftp.put(src_dir,des_dir)
        t.close()

if __name__ == '__main__':
    raw = input('请选择功能:1.执行命令  2.批量上传文件到主机 ').strip()
    if raw == '1':
        cmd()
    elif raw == '2':
        send()
    else:
        exit()
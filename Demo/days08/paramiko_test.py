'''
import paramiko,threading,time

#class conn(object):

def put(func):
    t = paramiko.Transport(func)
    t.connect(username = "root", password = "youxia")
    sftp = paramiko.SFTPClient.from_transport(t)
    #path1 = input('please input src: ').strip()
    #path2 = input('please input dsc: ').strip()
    remotepath='/tmp/test.txt'
    localpath='/tmp/test.txt'
    sftp.put(remotepath, localpath)
    #sftp.put(path1,path2)
    t.close()
def cmd(func):
    t = paramiko.Transport(func)
    t.connect(username = "root", password = "youxia")
    stdin, stdout, stderr = t.exec_command('df')
    # 获取命令结果
    result = stdout.read()

    # 关闭连接
    t.close()


threads = []
t1 = threading.Thread(target=put,args=(("10.37.129.6",22),))
t2 = threading.Thread(target=put,args=(("10.37.129.7",22),))
threads.append(t1)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()
        t.join()
'''

import paramiko
import os
import datetime
from configparser import ConfigParser
ConfigFile='config.ini'
config=ConfigParser()
config.read(ConfigFile)
hostname1=''.join(config.get('IP','ipaddress'))
address=hostname1.split(';')
print(address)
username='root'
password='youxia'
port=22

if __name__=="__main__":
        for ip in address:
                paramiko.util.log_to_file('paramiko.log')
                s=paramiko.SSHClient()
                s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                s.connect(hostname=ip,username=username,password=password)
                stdin,stdout,stderr=s.exec_command('free;ifconfig;df -h')
                print(stdout.read())
                s.close()
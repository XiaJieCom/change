
'''
z = zipfile.ZipFile('ts.zip','w')
z.write('ab.log')
z.write('as.txt')
z.close()
'''
'''
z = zipfile.ZipFile('ts.zip','r')
z.extractall()
z.close()
'''
'''
import shutil

#指定压缩后的文件名/压缩方法/源路径
ret = shutil.make_archive('test','zip',root_dir='/Users/jack/Documents/git/github/Demo/days06/test')
#指定压缩后的目标路径和文件名/压缩方法/源路径
ret = shutil.make_archive('/Users/jack/Documents/git/github/Demo/days06/ss','zip',root_dir='/Users/jack/Documents/git/github/Demo/days06/test')

#区别   压缩后放置当前程序目录

#解压
import zipfile
z = zipfile.ZipFile('test.zip','r')
z.extractall()
z.close()
'''
'''
import shelve

d = shelve.open('shelve_test') #打开一个文件

class Test(object):
    def __init__(self,n):
        self.n = n


t = Test(123)
t2 = Test(123334)

name = ["alex","rain","test"]
d["test"] = name #持久化列表
d["t1"] = t      #持久化类
d["t2"] = t2

d.close()
'''


import xml.etree.ElementTree as et

tree = et.parse('t1.xml')
root = tree.getroot()
#print(root.tag)

#遍历整个文档
'''
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.text)
'''
#遍历rank节点
'''
for node in root.iter('rank'):
    print(node.tag,node.text)
'''

'''
#修改节点
for node in root.iter('rank'):
    print(node.tag,node.text)
    new_rank = int(node.text) + 10
    node.text = str(new_rank)
    node.set('update','sss')
tree.write('t2.xml')
'''
#删除节点
'''
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 60 :
        root.remove(country)
tree.write('t3.xml')
'''
'''
import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {
    'ServerAliveInterval':'45',
    'Compression':'yes',
    'ComressionLevel':'9'
}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topSecret.server.com'] = {}
topSecret = config['topSecret.server.com']
topSecret['Host Port'] = '3306'
topSecret['ForwardX11'] = 'no'
config['DEFAULT']['ForwardXll'] = 'yes'
with open('ss1.cfg','w') as configfile:
    config.write(configfile)
'''
'''
import hashlib

h = hashlib.md5()
h.update(b'haha')
h.update(b'enenen')

msg = h.digest()
msg1 = h.hexdigest()
print(msg)

'''
import subprocess
import logging

logging.debug('this is a debug messages!')
logging.info('this is a info messages!')
logging.warning('this is a warning messages!')
logging.critical('this is  a critical messages!!!')

logging.basicConfig(format='%(asctime)s %(message)s',datefmt='%Y-%m-%d %H:%M',filename='access.log',level=logging.INFO)
logging.debug('This messages should go to the access.log!')
logging.info('This is info!')
logging.warning('This is warning')

logger = logging.getLogger('Test')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

fh = logging.FileHandler('access.log')
fh.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

logger.debug('debug')
logger.info('info..')
logger.warn('warn!')
logger.error('error!!')
logger.critical('critical!!!')

'''

class Role(object):
    def __int__(self,name,role,weapon,life_value):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
    def buy_weapon(self,weapon):
        print('%s is buy [%s]'%(self.name,weapon))
        self.weapon = weapon
p1 = Role('tom','Police','b10',100)
t1 = Role('jack','Terrorist','b10',50)
p1.buy_weapon('ak47')
t1.buy_weapon('m4a1')


'''

'''
1.个不同角色

2.冲突

3.不同交互产生不同的行为

'''


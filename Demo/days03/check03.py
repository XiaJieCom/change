__author__ = 'jack'

import json
import collections
from collections import defaultdict
def conf(*args):
    #将整个配置文件放入一个列表
    conf_list = []
    with open('test.log') as f:
        for i  in f.readlines():
            conf_list.append(i)
    return conf_list

def record(*args):
    res = conf(raw)
    d = json.loads(raw)
    for v in d.items():
        #print('\n%s%s'%(type(v),v))
        for i in v:
            #print(type(i),i)
            if type(i) == str and i != 'record' and i != 'backend':
                server_name = i
                #print(server_name,' ',end="")
            if type(i) == dict:
                for k,v in i.items():
                    print(k,v,'',end="")

def select(*args):
    res = conf(raw)
    for i in res:
       if 'backend' in i and 'use_backend' not in i:
            if raw in i:
                print('\n %s'%(i))
                print(res[res.index(i)+1])
choice =int(input("1、获取HA记录\n2、增加HA记录\n3、删除HA记录\n请输入你的选择: ").strip())

if choice == 1:
    #print("这里是HA记录")
    raw = input("请输入要查询的域名")
    select(raw)
    '''
    res = conf(raw)
    for i in res:
       if 'backend' in i and 'use_backend' not in i:
            if raw in i:
                print('\n%d %s'%(res.index(i),i))
                print(res.index(i)+1,res[res.index(i)+1])
                '''
    pass
elif choice == 2:
    #print('增加HA记录')
    raw = input('请输入你要添加的记录： ')
    d = json.loads(raw)
    for v in d.items():
        #print('\n%s%s'%(type(v),v))
        for i in v:
            #print(type(i),i)
            if type(i) == str and i != 'record' and i != 'backend':
                server_name = i
    res = conf(raw)
    for i in res:
        if 'backend' in i and 'use_backend' not in i:
            if server_name in i:
                print(i)
                print(conf().index(i)+1)
                #conf().insert(conf().index(i),server_name)
                conf().append(server_name)
                for i in conf():
                    print(i)
                #print(conf()[3])
                '''
                print('\n %s'%(i))
                print(conf()[conf().index(i)],conf().index(conf()[conf().index(i)]))
                print(conf()[conf().index(i)+1],conf().index(conf()[conf().index(i)+1]))
                print(conf()[conf().index(i)+2],conf().index(conf()[conf().index(i)+2]))
'''


    #raw = '{"backend":"www.oldboy.org","record":{"server": "100.1.7.999","weight": 20,"maxconn": 30}}'
   # res = conf(raw)
    #print(res)
    #re = record()




    '''
    for i in res:

       if 'backend' in i and 'use_backend' not in i:
            if raw in i:
                print(res[res.index(i)])
                print(res[res.index(i)+1])
                res.insert(res.index(i)+1,raw)
                print(res[res.index(i)+1])

        if 'backend' in i and 'use_backend' not in i:
            print(i)
        '''











    pass
else:
    print('删除HA记录')
    pass
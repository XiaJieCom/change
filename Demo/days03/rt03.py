import json

def conf(*args):
    #将整个配置文件放入一个列表
    conf_list = []
    with open('test.log') as f:
        for i  in f.readlines():
            conf_list.append(i)
    return conf_list
def backend(*args):
    #通过接收到的server_name 取出记录
    for i in res:
       if 'backend' in i and 'use_backend' not in i:
            if server_name in i:
                print('\n %s'%(i))
                print(res[res.index(i)+1])
choice =int(input("1、获取HA记录\n2、增加HA记录\n3、删除HA记录\n请输入你的选择: ").strip())

if choice == 1:
    #print("这里是HA记录")
    ha = input("请输入要查询的域名：")
    res = conf(ha)
    for i in res:
       if 'backend' in i and 'use_backend' not in i:
            if ha in i:
                print('\n %s'%(i))
                print(res[res.index(i)+1])
    pass
elif choice == 2:
    #print('增加HA记录')
    #raw = input('请输入你要添加的记录： ')
    raw = '{"backend":"test.oldboy.org","record":{"server": "100.1.7.999","weight": 20,"maxconn": 30}}'
    res = conf()
    d = json.loads(raw)
    for v in d.items():
        #print('\n%s%s'%(type(v),v))
        for i in v:
            #print(type(i),i)
            if type(i) == str and i != 'record' and i != 'backend':
                server_name = i

    #print(server_name)
    reg = conf(server_name)
    #取出带有server_name的记录
    #print(res)
    backend(reg)
    #匹配出只带有server_name的记录
    for i in conf():
        if server_name in i:
            print(i)
        else:
            conf().append('backend %s'% server_name)
            for sn in conf():
                print(sn)


    #添加到文件的功能没有实现
    #之前的想法是把整个文件格式化为一个list，然后通过查询到的backend记录的index，来指定插入位置；
    #但是功能实现过程中，无法按想法添加





    pass
else:
    print('删除HA记录')
    pass
__author__ = 'jack'
import json
def backend(*args):
    input_list = 'backend %s' % raw
    conf_list = []
    with open('test.log') as f:
        for k in f:
            k = k.strip()
            if k == input_list:
                continue
    return k
raw = '{"backend":"test.oldboy.org","record":{"server": "100.1.7.999","weight": 20,"maxconn": 30}}'

d = json.loads(raw)
def record():
    for v in d.items():
        #print('\n%s%s'%(type(v),v))
        for i in v:
            #print(type(i),i)
            if type(i) == str and i != 'record' and i != 'backend':
                server_name = i
                print(server_name,' ',end="")
            elif type(i) == dict:
                for k,v in i.items():
                    print(k,v,'',end="")
record()
'''


for v in d.items():
    #print(v)
    for i in v:
        if type(i) == dict:
            for k,v in i.items():
                print(k,v)
'''
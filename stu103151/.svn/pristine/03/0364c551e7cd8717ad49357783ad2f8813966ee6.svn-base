import json,os,sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf  import settings

def read():
    with open(settings.CONFIG, "r") as f:
        config = json.load(f)
    return config
def write(host):
    if type(host) == dict:
        pop_list = []
        for k in host:
            host[k] = list(set(host[k]))
            #print('this is k %s '%host[k])
            if not host[k]:
                pop_list.append([k])
                print(pop_list)
        for i in pop_list:
            host.pop(i)
            #print('This is i %s '%i)
        with open(settings.CONFIG,'w') as f:
            json.dump(host,f)
    else:
        raise TypeError



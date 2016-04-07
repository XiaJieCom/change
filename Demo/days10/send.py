import rpyc
from rpyc import Service
from rpyc.utils.server import ThreadedServer
import os
class Test(Service):
    def exposed_cmd(self,cmd):  #客户端要调用的函数方法前面要加‘exposed_’，否则调用失败！
        return os.system(cmd)

sr = ThreadedServer(Test, port=9990, auto_register=False)
sr.start()
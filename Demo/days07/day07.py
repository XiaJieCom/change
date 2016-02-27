
'''
class Aniaml:
    count = 10
    def __init__(self,name):
        self.name = name
        self.num = None
    hobbie = 'meat'
    @classmethod    #类方法,不能访问实例变量
    def talk(self):
        print('%s is talking ...'%self.hobbie )
    @staticmethod   #静态方法,不能访问类变量及实例变量
    def walk():
        print('is walking ...')
    @property   #把方法变属性
    def habbit(self):
        print('%s habit is sss'%self.name)
    @property
    def total_players(self):
        return self.num
    @total_players.setter
    def total_players(self,num):
        self.num = num
        print('total players:',self.num)
    @total_players.deleter
    def total_players(self):
        print('total player got deleted.')
        del self.num
Aniaml.hobbie
Aniaml.talk()

d = Aniaml('hahah')
print(d.total_players)
d.total_players = 3

del d.total_players
print(d.total_players)

'''
''''
class A:
    n = 'A'
    def f2(self):
        print('f2 from A')
class B(A):


    n = 'B'
    def __init__(self):
        pass
    def f1(self):
        print('f1 from B')
    def f2(self):
        print('f2 from B')
    def __del__(self):
        print('del ....')
    def __call__(self, *args, **kwargs):
        print('__cal__')
class C(A):
    n = 'C'
    def f2(self):
        print('f2 from C')
class D(B,C):
    pass
d = D()
d.f1()
d.f2()
print(B.__doc__)
print(B.__dict__)
print(B.__class__)
print(B.__module__)
B.__del__
obj = B()
obj()
'''



import sys

class WebServer(object):
    def __init__(self,host,port):
        self.host = host
        self.port = port
    def start(self):
        print('Server is stating ...')
    def stop(self):
        print('Server is stopping ...')
    def restart(self):
        self.stop()
        self.start()
        print('Server is restarting ...')


def test_run(self,name):
    print('Test_running ...',name,self.host)
if __name__ == '__main__':
    server = WebServer('localhost',80)
    if hasattr(server,sys.argv[1]):
        func = getattr(server,sys.argv[1])
        func()
    setattr(server,'run',test_run)
    server.run(server,'haha')
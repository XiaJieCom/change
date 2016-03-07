'''
while True:
    n1 = input('input a number: ')
    n2 = input('input a number: ')



    try:
        n1 = int(n1)
        n2 = int(n2)
        res = n1 + n2
        print(res.sd)
        l = [1,2,3,4,]
        print(l[10])

        d = {1:'a',2:'b'}
        print(d[3])
        print('num:%s' %res)
    except ArithmeticError as e:
        print('ArithmeticError')
    except IndexError as e:
        print('IndexError')
    except KeyError as e:
        print('KeyError')
    except ValueError as e:
        print('ValueError',e)
    except Exception as e:
        print('异常错误')
        print(e)
'''
#自定义异常
class DemoException(Exception):
    def __init__(self,msg):
        self.message = msg
    def __str__(self):
        return self.message
a = 1
try:
    #如果不满足该条件,抛出异常
    assert a == 1
except DemoException as e:
    print(e)
else:
    print('ok')
#无论是否存在异常,都执行finally
finally:
    print('over')
__author__ = 'jack'
'''
1、打开两个文件
2、把backend 部分之前写入
3、把backend列表处理，最后再写入



'''


"""
1、迭代器、生成器
2、装饰器
    http://www.cnblogs.com/wupeiqi/articles/4980620.html
3、递归
4、算法
5、正则
6、常用模块
    http://www.cnblogs.com/wupeiqi/articles/4963027.html
"""
'''
三元运算符，简单if else语句
if 1 ==1:
    name = 'haha'
else:
    name = 'sss'

name = 'xxx' if 1 == 1 else 'ddd'
print(name)
'''
'''
lambda  简单函数
def ts(arg):
    return arg +1
res = ts(1111)
print(res)

lam = lambda arg:arg + 1
res = lam(123)
print(res)
'''

#迭代器
'''
ts = iter(['asd','sds','qweq'])

print(ts.__next__())
print(ts.__next__())
print(ts.__next__())
print(ts.__next__())
'''
'''
def cash(m):
    while m > 0:
        m -=1
        yield 100
        print('取钱')
atm = cash(300)
print(type(atm))
print(atm.__next__())
print(atm.__next__())
print('待会............')
print(atm.__next__())
'''
'''
import time
def consumer(name):
    print('%s,过来吃饭' %name)
    while True:
        baozi = yield
        print('包子[%s]来了，被[%s]吃了' %(baozi,name))
def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print('开始做饭了')
    for i in range(10):
        time.sleep(1)
        print('做了2个包子')
        c.send(i)
        c2.send(i)
producer('tom')
'''
'''
def login(func):
    print('Success!')
    return func
def tv():
    print('welcome to page!')

tv = login(tv)
tv()

'''
'''

def login(func):
    def inner(arg):
        print('Success!')
        func(arg)
    return inner
@login
def tv(name):
    print('welcome [%s] to page!'%name)

#tv = login(tv)
tv('tom')

'''
'''
def before(request,kargs):
    print('before')
def after(request,kargs):
    print('after')
def filter(before_func,after_func):
    def outer(main_func):
        def wrapper(request,kargs):
            before_result = before_func(request,kargs)
            print('before ....')
            main_result = main_func(request,kargs)
            print('main ....')
            after_restut = after_func(request,kargs)
            print('after ...')
        return wrapper
    return outer
@filter(before,after)
def Index(request,kargs):
    print('index')
Index('xx','aa')

'''
'''
递归
def calc(n):
    print(n)
    if n/2 > 1:
        res = calc(n/2)
        print('res',res)
    print('N',n)
    return n
calc(10)


'''
'''
斐波那契数列
'''
'''
def func(arg1,arg2,stop):
    if arg1 == 0:
        print(arg1)
    arg3 = arg1 + arg2
    print(arg3)
    if arg3 < stop:
        func(arg2,arg3,stop)
func(0,1,100)
'''
'''
def search(data_soure,find_n):
    mid = int(len(data_soure)/2)
    print(len(data_soure))
    if len(data_soure) >=1:
        if data_soure[mid] > find_n:
            print('in left')
        #    print(data_soure[:mid])
            search(data_soure[:mid],find_n)
        elif data_soure[mid] < find_n:
            print('in right')
        #    print(data_soure[mid:])
            search(data_soure[mid:],find_n)
        else:
            print('Found in!')
    else:
        print('No!')
if __name__ == '__main__':
    data = list(range(1,10000000))
    search(data,1)
'''
'''
data = [[col for col in range(4)] for row in range(4)]
for r_index,row in enumerate(data):
    for c_index in range(r_index,len(row)):
        tmp = data[c_index][r_index]
        data[c_index][r_index] = row[c_index]
        data[r_index][c_index] = tmp
    print('*****************')
    for r in data:print(r)
'''
"""
1、小括号   先计算小括号
先找到所有的括号    最里层的括号
+ —— 作为分隔符， 切割成列表
    计算乘除
算出来之后再把+——放回去

递归



执行流程如下：
******************** 请计算表达式： 1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ) ********************
before： ['1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
-40.0/5=-8.0
after： ['1-2*((60-30+-8.0*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
========== 上一次计算结束 ==========
before： ['1-2*((60-30+-8.0*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
9-2*5/3+7/3*99/4*2998+10*568/14=173545.880953
after： ['1-2*((60-30+-8.0*173545.880953)-(-4*3)/(16-3*2))']
========== 上一次计算结束 ==========
before： ['1-2*((60-30+-8.0*173545.880953)-(-4*3)/(16-3*2))']
60-30+-8.0*173545.880953=-1388337.04762
after： ['1-2*(-1388337.04762-(-4*3)/(16-3*2))']
========== 上一次计算结束 ==========
before： ['1-2*(-1388337.04762-(-4*3)/(16-3*2))']
-4*3=-12.0
after： ['1-2*(-1388337.04762--12.0/(16-3*2))']
========== 上一次计算结束 ==========
before： ['1-2*(-1388337.04762--12.0/(16-3*2))']
16-3*2=10.0
after： ['1-2*(-1388337.04762--12.0/10.0)']
========== 上一次计算结束 ==========
before： ['1-2*(-1388337.04762--12.0/10.0)']
-1388337.04762--12.0/10.0=-1388335.84762
after： ['1-2*-1388335.84762']
========== 上一次计算结束 ==========
我的计算结果： 2776672.69524

http://crm.oldboyedu.com/crm/survery/4/
"""
'''
def t1(a):
    def t2(b):
        return a+b
    return t2
f = t1('aaaa_')
res = f('bbbbbb')
print(res)

'''
'''
def action(x):
    return(x)

def action_pro(n):
    def warpper(x):
        return(n(x) * x)
    return(warpper)

action = action_pro(action) #第一个action为自定义的伪装变量，第二个action为上边定义的action函数
res = action(3) #此函数实际为warpper(3)，返回值为9
print(res)

'''
'''
def login(func):
    def inner(arg):
        print('Success!')
        func(arg)
    return inner
@login
def tv(name):
    print('welcome [%s] to page!'%name)

#tv = login(tv)
tv('tom')
'''
import re

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello world!')

if match:
    # 使用Match获得分组信息
    print(match.group())

### 输出 ###
# hello
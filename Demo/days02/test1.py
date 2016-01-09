__author__ = 'jack'
'''
import  sys

print(sys.argv)
传入的是列表
python3 test1.py 80 8080
['test1.py', '80', '8080']
'''
'''
import  sys
print(sys.argv)
'''

"""
元组的元素不可以被修改；
原则的元素的元素可以被修改
"""
'''
t1 = (2,3,4,5,{'kk':'a','c':'d'})
print(t1)
print(t1[4])

t1[4]['kk'] = 'haha'
print(t1)
'''
"""

类-对象关系


"""
'''

divmod 取商，取余
num = 29
res = num.__divmod__(5)
print(res)
'''
'''
abs 绝对值
    _abs_()
    abs()

num = -10
res = num.__abs__()
print(res)

res = abs(num)
print(res)
'''
'''
加
    _add_()
    +
res = num.__add__(10)
print(res)
res = num + 10
print(res)

'''
"""
type 获取类

dir 获取成员
"""
'''
a = 'hahah'
print(type(a))
print(dir(a))
'''
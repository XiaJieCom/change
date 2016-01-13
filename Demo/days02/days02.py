__author__ = 'jack'
'''
import  sys

print(sys.argv)
传入的是列表
python3 days02.py 80 8080
['days02.py', '80', '8080']
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
"""
count
    统计出现次数
name = "xiaominghahah"
res = name.count('a')
print(res)
name = "xasdsadasdasd"
res = name.count('a',2,10)


__contains__()
    包含
res = name.__contains__('a')
print(res)
res = name.__contains__('b')
print(res)

casefold()
    大写转小写
name = "xIIaominghahah"
res = name.casefold()

center()
    输出到中间位置
name = "xIIao"
res = name.center(20,'*')
    输出
*******xIIao********

encode()
    输出为encode
name = "小明"
res = name.encode()
print(res)


endswith()
    判断是否以某某字符串结尾，可以选择起始结束位置
name = "xasdsadasdasd"
res = name.endswith('c',2,10)
print(res)
"""
"""
列表
append()
    添加
l = [1,2,3,4,5]
l.append('haha')
print(l)
extend()
    扩展，合并多个列表
l = [1,2,3,4,5]
b = [3,4,6,7,31]
l.extend(b)
print(l)
"""
'''
num = [11,22,33,44,55,66,77,88,99,100,101,102,]
num_max = []
num_min = []
dic = {}
for i in num:
    #print(i)
    if i > 66:
        num_max.append(i)
        dic.setdefault('k1',num_max)
    else:
        num_min.append(i)
        dic.setdefault('k2',num_min)
#print(num_max)
print(dic)


'''
"""
作业
1、博客
2、购物车
    商品展示，
    价格，
    买，
    加入购物车，
    付款，钱不够
3、预习set/文件操作/calations
    寻找差异，字典和set



"""

shopping_dict = {
    "酒":{
        '啤酒':[('黑啤酒',10),('扎啤',5),('白啤',15)],
        '红酒':[(82,10000),(90,5000),(100,500),],
        '白酒':[('茅台',500),('五粮液',600),('海之蓝',200)]
        },
    "饮料":{
        '可乐':[('百事可乐',3.5),('可口可乐',3.5),('非常可乐'),'3.5'],
        'tea':[('lv tea',10),('hong tea',8),('普洱',20)],
        '水':[('哇哈哈',3),('农夫山泉',2),('康师傅',2.5)]
    },
    "手机":{
        '智能机':[('T1',2999),('iPhone',4800),('MX 4',1999),],
        '平价机':[('红米',799),('坚果',699),('note',599)],
        '功能机':[('金立',100),('诺基亚 101',200),('三星',150)]
    }
}
'''
f_list = []
s_list = []
t_list = []
for i in shopping_dict.keys():
    print(i)
    for i in shopping_dict[i].keys():
        print(i)
'''
for i in shopping_dict.items():
    print(type(i))












import random,time


f_name = {
    1:'优雅的',
    2:'蠢蠢的',
    3:'大耳朵',
    4:'小鼻子',
    5:'一只眼睛的',
    6:'凶恶的',
    7:'善良的',
    8:'可爱的',
    9:'萌萌的',
    10:'肥肥的',
}
l_name = {
    1:'兔子',
    2:'狐狸',
    3:'鼻涕虫',
    4:'骷髅战士',
    5:'亡灵骑士',
    6:'亡灵法师',
    7:'亡灵猎人',
    8:'亡灵召唤师',
    9:'强盗',
    10:'恶人',
}

f = random.randint(1,10)
l = random.randint(1,10)

print('你好,%s%s' %(f_name[f],l_name[l]))











'''try:
    input(s_aside)
except SyntaxError:
    pass
'''

#end=time.time()
#pt=end-start
#print("程序运行时间：",pt)
'''
try:
    input("按回车退出")
except SyntaxError:
    pass
'''
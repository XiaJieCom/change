__author__ = 'jack'
"""
字符串本质上是字符数组

set 是一个无序且不重复的元素集合
访问速度快；天生解决元素重复问题

"""
'''
set
add
clear
difference
'''
'''
s1 = set([1,3,2,4,5,6,])
s2 = set([1,2,3,4,5,6,'hahahah'])

print(s1)
print(s2)
s3 = s1.difference([1])
print(s3)
'''
"""
1、原来没有  新加入
2、原来有 跟新
3、新没有，原来有 原来删除

要更新的数据列表
要删除的
要添加
"""
'''
old_dict = {
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#2":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 }
}

# cmdb 新汇报的数据
new_dict = {
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 800 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#4":{ 'hostname':'c2', 'cpu_count': 2, 'mem_capicity': 80 }
}
old = set(old_dict.keys())
new = set(new_dict.keys())
update_set = old.intersection(new)
print(update_set)
#intersection old和new对比，取出共同交集
delete_set = old.symmetric_difference(update_set)
print(delete_set)
#symmetric_difference old和update_set 对比，取出不同的部分
add_set = new.symmetric_difference(update_set)
print(add_set)
#symmetric_difference new和update_set的对比，取出不同的部分
'''
'''
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
def mail():
    ret = True
    try:
        msg = MIMEText('邮件内容','plain','utf-8')
        msg['From'] = formataddr(['wo','13121889803@163.com'])
        msg['To'] = formataddr(['Test','13121889803@163.com'])
        msg['Subject'] = '主题'
        server = smtplib.SMTP('smtp.163.com',25)
        server.login("13121889803@163.com",'xiajieak@163.com')
        server.sendmail('13121889803@163.com',['13121889803@163.com',],msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret
ret = mail()
if ret:
    print("Success!")
else:
    print("Try again!")
'''
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
'''
def mail(f_user,t_user):
    ret = True
    try:
        msg = MIMEText('邮件内容','plain','utf-8')
        msg['From'] = formataddr(['wo',f_user])
        msg['To'] = formataddr(['Test',t_user])
        msg['Subject'] = '主题'
        server = smtplib.SMTP('smtp.163.com',25)
        server.login(f_user,'hahah@163.com')
        server.sendmail(f_user,[t_user,],msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret
ret = mail('13121889803@163.com','13121889803@163.com')
if ret == True:
    print("Success!")
else:
    print("Try again!")

'''
'''
def num():
    res = True
    try:

    except Exception:
        res = False
    return res
res = num()
print(res)
if res:
    print("OK")
else:
    print("False")
'''
import json
import re
import collections
from collections import defaultdict
'''
ha_list = []
read = input("Input backend: ").strip()
with open('ha.conf','r') as ha:
    for i in ha.readlines():
        ha_list.append(i)
for i in ha_list:
    #print(ha_list.index(i),i)
    if read in i:
       # pattern = re.compile(r'backend ')
       # mactch = pattern.match(i)
        print(i)
'''
'''
def show(*args,**kwargs):
    print(args,type(args))
    print(kwargs,type(kwargs))
l = [1,2,3,3434,343,]
d = {'k1':100,'k2':20}
show(*l,**d)
'''
'''
import json
inp_str = "[11,22,33,44]"
inp_list = json.loads(inp_str) # 根据字符串书写格式，将字符串自动转换成 列表类型


inp_str = ' {"k1":123, "k2": "wupeiqi"} '  # 正确的输入      切记，内部必须是 双引号 ！！！
#inp_str = " {'k1':123, 'k2': 'wupeiqi'}"   # 错误的输入
inp_dict = json.loads(inp_str) # 根据字符串书写格式，将字符串自动转换成 字典类型
'''

raw = {"backend": "test.oldboy.org","record":{"server": "100.1.7.999","weight": 20,"maxconn": 30}}

d = json.loads()













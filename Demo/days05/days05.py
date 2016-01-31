'''
模式	描述
^ 	匹配字符串的开头
$ 	匹配字符串的末尾。
. 	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
[...] 	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...] 	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
re* 	匹配0个或多个的表达式。
re+ 	匹配1个或多个的表达式。
re? 	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
re{ n}
re{ n,} 	精确匹配n个前面表达式。
re{ n, m} 	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
a| b 	匹配a或b
(re) 	G匹配括号内的表达式，也表示一个组
(?imx) 	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
(?-imx) 	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
(?: re) 	类似 (...), 但是不表示一个组
(?imx: re) 	在括号中使用i, m, 或 x 可选标志
(?-imx: re) 	在括号中不使用i, m, 或 x 可选标志
(?#...) 	注释.
(?= re) 	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
(?! re) 	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
(?> re) 	匹配的独立模式，省去回溯。
\w 	匹配字母数字
\W 	匹配非字母数字
\s 	匹配任意空白字符，等价于 [\t\n\r\f].
\S 	匹配任意非空字符
\d 	匹配任意数字，等价于 [0-9].
\D 	匹配任意非数字
\A 	匹配字符串开始
\Z 	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。c
\z 	匹配字符串结束
\G 	匹配最后匹配完成的位置。
\b 	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B 	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\n, \t, 等. 	匹配一个换行符。匹配一个制表符。等
\1...\9 	匹配第n个分组的子表达式。
\10 	匹配第n个分组的子表达式，如果它经匹配。否则指的是八进制字符码的表达式。
'''

'''

import re

'''

'''
num1 = '15121889203'
m = re.search(r'(1)([34578]\d{9})',num1)
print(m.group())
ip1 = '192.168.1.102323'
'''

'''
m = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ip1)
print(m.group())
mail = '1231231ad.sd@163.com'
m = re.search(r"[0-9.a-z]{0,26}@[0-9.a-z]{0,20}.[0-9a-z]{0,8}", mail)
print(m.group())

'''
'''
data = [10,4,33,21,54,3,8,11,5,22,2,1,17,13,6]
#for j in range(len(data)):
for j in range(1,len(data)):
    #for i in range(len(data)-1):
    for i in range(len(data)-j):
        if data[i] > data[i+1]:
            tmp = data[i]
            data[i] = data[i+1]
            data[i+1] = tmp
    print(data)
print(data)
'''
'''
import time
import datetime
print('处理器时间: %s'%time.clock())
print('处理器时间: %s'%time.process_time())
print('时间戳: %s'%time.time())
print('当前系统时间: %s'%time.ctime())
print('昨天的现在时间: %s'%time.ctime(time.time()-86400))
print(time.gmtime(time.time()))

'''
'''
import random
print(random.random())
print(random.randint(1,3))

checkcode = ''
for i in range(4):
    current = random.randint(0,4)
    if current != i:
        tmp = chr(random.randint(65,90))
    else:
        tmp = random.randint(0,9)
    checkcode += str(tmp)
print(checkcode)
'''
import os
print(os.getcwd())
print(os.curdir)
print(os.pardir)
print(os.stat('days05.py'))
print(os.sep)
print(os.linesep)
print(os.pathsep)
print(os.name)
print(os.system("bash command"))
print(os.environ)
print(os.path.abspath(__file__))
print(os.path.isabs(__file__))





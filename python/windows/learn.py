# -*- coding: utf-8 -*-
import re
import urllib
'''
urllib.urlopen 获取类文件对象
read() 读取文件内容
info() 获取网页header信息
getcode() 获取网页状态码
geturl() 获取传入的网址的URL
#保存网页的两种方式，urlretrieve 和open文件的方式
#html = urllib.urlopen(url).read().decode('gbk','ignore').encode('utf-8')
#print html
#urllib.urlretrieve(html,'D:\\Document\\python\\tmp\\ts.html')
1、传入网址，字符串
2、传入的，文件名
3、一个函数的调用。
    a、目前为此传递的数据块数量
    b, 每个数据库的 大小，单位byte。%2.f 小数点保留2位；最后的“，” 保证显示在同一行
    c,远程文件的大小
'''
def callback(a,b,c):
    '''
        a，目前为此传递的数据块数量
        b, 每个数据库的 大小，单位byte。%2.f 小数点保留2位；最后的“，” 保证显示在同一行显示
        c，远程文件的大小
    '''
    down_progress = 100.0*a*b/c
    if down_progress > 100:
        down_progress = 100
    print '%.2f%%' % down_progress,

#url = 'http://www.iplaypython.com'
url = 'http://www.sina.com'
url1 = 'http://www.jd.com'
url2 = 'http://www.amzon.com' 
local = 'D:\\Document\\python\\tmp\\ts.html'
urllib.urlretrieve(url,local,callback)
code = urllib.urlopen(url)
print code.info()


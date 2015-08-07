# coding:utf-8
import re
import requests


r = requests.get('http://bbs.zol.com.cn/dcbbs/')
data = r.text


link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,data)
for url in link_list:
    print url


'''
# coding:utf-8
import random
import urllib
import urllib2
from bs4 import BeautifulSoup

local = 'D:/Document/Linux/python/tmp/'
url = 'http://bbs.zol.com.cn/dcbbs'

my_headers = [
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    'ELinks/0.12pre5 (textmode; Linux; -)'
]

def get_conent(url, headers):
    random_header = random.choice(headers)
    req = urllib2.Request(url)
    req.add_header('User-Agent', random_header)
    req.add_header('Host', 'bbs.zol.com.cn')
    req.add_header(
        'Referer', 'http://bbs.zol.com.cn/dcbbs/')
    req.add_header('GET', 'url')
    content = urllib2.urlopen(req).read().decode('gbk', 'ignore').encode('utf-8')
    return content

def get_html_link(info):
    soup = BeautifulSoup(info)
    all_link = soup.find_all('li')
    for txt in all_link:
        cont = str(txt)
        head = cont.find(r'href="http://bbs.zol.com.cn/dcbbs/')
        end = cont.find(r'html', head)
        hlist = cont[head +6:end + 4]
        print hlist
info = get_conent(url, my_headers)
print get_html_link(info)
'''

'''
<li class="category-pic-6">
<a href="http://bbs.zol.com.cn/dcbbs/d21_483.html#picIndex3" target="_blank">
<img alt="xxxxx" height="116" src="http://i0.bbs.fd.zol-img.com.cn/g2/M00/05/0C/ChMlWVXBz3uIEIKqAABupGj0rVIAAIRGAA2QasAAG68896.jpg" width="217"/>
<span class="pic-title"><em>xxxx</em></span>
</a>
</li>
'''

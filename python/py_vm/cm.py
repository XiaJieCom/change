# -*- coding: utf-8 -*-
import re
import time
import urllib
import urllib2
import random

url = 'https://www.caimao.com/p2p/targetPage.htm?_=1438691179898'

my_headers = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
    'ELinks/0.12pre5 (textmode; Linux; -)'
]


def getContent(url,headers):

    random_header = random.choice(headers)
    print random_header

    req = urllib2.Request(url)
    req.add_header('User-Agent', random_header)
    req.add_header('Host', ' www.caimao.com')
    req.add_header('Referer', 'http://www.caimao.com/')
    req.add_header('GET', 'url')

    content = urllib2.urlopen(req).read()
    return content

info = getContent(url, my_headers)


def getCode(info):
    head = info.find(r'span class="select')
    end = info.find(r'</b', head)
    con = info[head + 62:end]
    # while True:
    i = 0
    while i < 300:
        print i
        if int(con) != 0:
            print 'Come on !!!'
            print con
        time.sleep(3)
        i = i + 1
    # return con

print getCode(info)
'''
<span class="select">
<i></i>
满标项目 (
<b id="totalTargetB">240</b>
)
</span>
'''

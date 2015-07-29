#!/usr/bin/env python

import urllib

i = 0
con = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html').read()
title = con.find(r'<a title=')
print title
href = con.find(r'href=',title)
html = con.find(r'.html',href)
url = con[href +6 :html +5 ]
print url

while i < 50:
    
    title = con.find(r'<a title=',html)
    href = con.find(r'href=',title)
    html = con.find(r'.html',href)
    url = con[href +6 :html +5 ]
    print url

    i = i + 1


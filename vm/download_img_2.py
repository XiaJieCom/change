# -*- coding: utf-8 -*-
import urllib2
import random


url = 'http://blog.csdn.net/happydeer'


my_headers = {
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
}


def get_content(url,headers):
    random_header = random.choice(headers)
    print random_header

    req = urllib2.Request(url)
    req.add_header("User-Agent",random_header)
    req.add_header("Host","blog.csdn.net")
    req.add_header("Referer","http://blog.csdn.net/")
    req.add_header("GET",url)

    content = urllib2.urlopen(req).read()
    return content
print get_content(url,my_headers)
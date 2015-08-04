# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup

url = 'http://tieba.baidu.com/p/2460150866'
#url = 'http://desk.zol.com.cn/bizhi/5679_70694_2.html'
#url = 'http://www.ithome.com/html/bizhi/164396.htm'


def get_content(url):
    html = urllib.urlopen(url)
    content = html.read().decode('gbk', 'ignore').encode('utf-8')
    html.close()
    return content


def get_img(info):
    soup = BeautifulSoup(info)
    all_img = soup.find_all('img')
    print len(all_img)
    for img in all_img:
        print img['src']


info = get_content(url)
print get_img(info)

'''
########################

con = urllib.urlopen(url)
print con.info()
print con.getcode()
img class="lazy" data-original="http://img.ithome.com/newsuploadfiles/2015/7/20150722_100038_730.jpg"
<a id="1366x768" class="current" href="/showpic/1366x768_70694_28.html" target="_blank" title="您当前的屏幕分辨率是：1366x768">1366x768</a>
<img alt="IT之家" height="28" src="http://img.ithome.com/images/v2.1/logo.png" width="65"/>
<img src="http://img.ithome.com/newsuploadfiles/2015/7/20150722_095916_590.jpg"/>
<img class="lazy" data-original="http://img.ithome.com/newsuploadfiles/2015/7/20150722_100038_730.jpg" src="http://img.ithome.com/images/v2/grey.gif"/>
<img class="lazy" data-original="http://img.ithome.com/newsuploadfiles/2015/7/20150722_100107_425.jpg" src="http://img.ithome.com/images/v2/grey.gif"/>
<img class="lazy" data-original="http://img.ithome.com/newsuploadfiles/2015/7/20150722_100548_51.jpg" src="http://img.ithome.com/images/v2/grey.gif"/>
<img class="lazy" data-original="http://img.ithome.com/images/v2.1/downsoftmaster.gif" src="http://img.ithome.com/images/v2/grey.gif"/>
'''

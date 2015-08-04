# -*- coding: utf-8 -*-
import re
import urllib

#url = 'http://tieba.baidu.com/p/2460150866'
url = 'http://desk.zol.com.cn/bizhi/5679_70694_2.html'

def get_content(url):
    html = urllib.urlopen(url)
    content = html.read().decode('gbk', 'ignore').encode('utf-8')
    html.close()
    return content

info = get_content(url)
print info


def get_img(info):
    regex = r'img src= "(.+?\.jpg)"'
    print regex
    pat = re.compile(regex)
    print pat
    images_code = re.findall(pat, info)
    #i = 0
    print images_code
    for img_url in images_code:
        print img_url
    #    urllib.urlretrieve(img_url, '%s.jpg' % i)
        i = i + 1

print get_img(info)

'''
con = urllib.urlopen(url)
print con.info()
print con.getcode()


<a id="1366x768" class="current" href="/showpic/1366x768_70694_28.html" target="_blank" title="您当前的屏幕分辨率是：1366x768">1366x768</a>
'''

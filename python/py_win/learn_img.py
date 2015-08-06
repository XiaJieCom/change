# -*- coding: utf-8 -*-
import re
import urllib

url = 'http://tieba.baidu.com/p/2460150866'


def get_content(url):
    html = urllib.urlopen(url)
    content = html.read()
    html.close()
    return content

info = get_content(url)


def get_img(info):
    regex = r'class="BDE_Image" src="(.+?\.jpg)"'
    pat = re.compile(regex)
    images_code = re.findall(pat, info)
    print images_code
    i = 0
    for img_url in images_code:
        print img_url
        urllib.urlretrieve(img_url, '%s.jpg' % i)
        i = i + 1
print get_img(info)

'''
con = urllib.urlopen(url)
print con.info()
print con.getcode()


<img class="BDE_Image" width="560" height="315" pic_ext="jpeg" src="http://imgsrc.baidu.com/forum/w%3D580/sign=37854f4d42166d223877159c76220945/82305c6034a85edfefcf36a548540923dc5475f2.jpg" pic_type="0">
'''

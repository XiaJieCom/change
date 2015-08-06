#coding=utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" src='
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for img in imglist:
        print img
    #return imglist

'''
    type (imglist)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
'''

html = getHtml("http://www.ithome.com/html/bizhi/164396.htm")

print getImg(html)


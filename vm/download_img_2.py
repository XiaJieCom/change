#!/usr/bin/env python
import re
import urllib
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
def getImg(html):
	reg = r'data-original="(.+?\.jpg)" />'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	i = 0
	for imgurl in imglist:
		name = imgurl[45:]
		print name
		content = urllib.urlopen(imgurl).read()
		open(r'tmp/' + name,'w+').write(content)
		i = i + 1
html = getHtml("http://www.ithome.com/html/bizhi/164396.htm")
print getImg(html)



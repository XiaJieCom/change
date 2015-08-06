# coding:utf-8
'''
import urllib
url = [''] * 40
i = 0
con = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html').read()
title = con.find(r'<a title=')
href = con.find(r'href=', title)
html = con.find(r'.html', href)

#url[0] = con[href + 6:html + 5]
#print url

while title != -1 and href != -1 and html != -1 and i < 40:
    url[i] = con[href +6 :html +5]
    print url[i]
    title = con.find(r'<a title=',html)
    href = con.find(r'href=',title)
    html = con.find(r'.html',href)
    i = i +1


'''
import urllib

i = 0
url = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'
con = urllib.urlopen(url).read()
title = con.find(r'<a title=')
href = con.find(r'href=', title)
html = con.find(r'.html', href)
url = con[href + 6:html + 5]
print url

while title != -1 and href != -1 and html != -1 and i < 50:

    title = con.find(r'<a title=', html)
    href = con.find(r'href=', title)
    html = con.find(r'.html', href)
    url = con[href + 6:html + 5]
    print url

    i = i + 1

import urllib
i = 0
con = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html').read()
title = con.find(r'<a title=')
href = con.find(r'href=',title)
html = con.find(r'.html',href)
url = con[href +6 :html +5 ]
print url
while title != -1 and href != -1 and html != -1 and i < 40:
    title = con.find(r'<a title=',html)
    href = con.find(r'href=',title)
    html = con.find(r'.html',href)
    url = con[href +6 :html +5 ]
    print url
    i = i + 1

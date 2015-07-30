#!/usr/bin/env python
import time
import urllib

i = 0
link = 1
page = 1
url = ['']*350
while page <= 7:
  con = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_'+str(page)+'.html').read()
  title = con.find(r'<a title=')
  href = con.find(r'href=',title)
  html = con.find(r'.html',href)
  while title != -1 and href != -1 and html != -1 and i < 350:
    url[i] = con[href +6 :html +5 ]
    print link,url[i]
    title = con.find(r'<a title=',html)
    href = con.find(r'href=',title)
    html = con.find(r'.html',href)
    content = urllib.urlopen(url[i]).read()
    open(r'/tmp/zhihu/'+url[i][-26:],'w+').write(content)
    time.sleep(5)
    link = link + 1
    i = i +1
  page = page + 1

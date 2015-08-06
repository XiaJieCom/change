#1、打印第一篇文章链接
import urllib
url = ['']*40
i = 0
url = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'
con = urllib.urlopen(url).read()
title = con.find(r'<a title=')
href = con.find(r'href=',title)
html = con.find(r'.html',href)
url = con[href +6 :html +5 ]
print url

#2.1打印第一页所有文章链接
import urllib
url = ['']*40
i = 0
url = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'
con = urllib.urlopen(url).read()
title = con.find(r'<a title=')
href = con.find(r'href=',title)
html = con.find(r'.html',href)
url[0] = con[href +6 :html +5 ]
print url

while title != -1 and href != -1 and html != -1 and i < 40:
    url[i] = con[href +6 :html +5 ]
    print url[i]
    title = con.find(r'<a title=',html)
    href = con.find(r'href=',title)
    html = con.find(r'.html',href)
    i = i +1
	
#2.2改编

import urllib

i = 0
url = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'
con = urllib.urlopen(url).read()
title = con.find(r'<a title=')
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
	
	


#3、下载知乎某一页的所有链接
#!/usr/bin/env python
import time
import urllib

i = 0
j = 0
url = ['']*30
name = ['']*30
html = 'http://www.zhihu.com/collection/19668036'
con = urllib.urlopen(html).read()
target = con.find(r'<a target="_blank')
base = con.find(r'href=',target)
end = con.find('>',base)

while target != -1 and base != -1 and end != -1 and i < 30:
  url[0] = 'http://www.zhihu.com' + con[target +25 :end - 1]
  name[0] =  con[base +16 :end - 1]
  target = con.find(r'<a target="_blank',end)
  base = con.find(r'href=',target)
  end = con.find('>',base)
  content = urllib.urlopen(url[0]).read()
  open(r'D:/Document/Linux/python/tmp/'+name[0]+'.html','w+').write(content)
  print 'Downloading ...',name[0]
  time.sleep(3)
  i = i + 1


#4、下载所有页上的所有链接

import time
import urllib

page = 1
url = ['']*350
i = 0
link = 1
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
    link = link + 1
    i = i +1
  else:
    print 'find end!'
  page = page + 1
else:
    print 'all find end'
j = 0
while j < 50:
    content = urllib.urlopen(url[j]).read()
    open(r'tmp/'+url[j][-26:],'w+').write(content)
    j = j + 1
    time.sleep(5)
else:
    print 'download over!'

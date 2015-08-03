#第一篇
import urllib

url = ['']*40

i = 0

con = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html').read()

title = con.find(r'<a title=')

href = con.find(r'href=',title)

html = con.find(r'.html',href)

url = con[href +6 :html +5 ]

print url

#第一页

import urllib
url = ['']*40
i = 0
con = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html').read()
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
	
#改编

import urllib

i = 0
con = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html').read()
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
	
	
#zhihu 
import urllib

i = 0
url = ['']*40
con = urllib.urlopen('http://www.zhihu.com/collection/19668036').read()
target = con.find(r'<a target="_blank')
base = con.find(r'href=',target)
end = con.find('>',base)
url[0] = 'http://www.zhihu.com' + con[target +25 :end - 1]
print url[0]


while i < 20:
  url[0] = 'http://www.zhihu.com' + con[target +25 :end - 1]
  print url[0]
  target = con.find(r'<a target="_blank',end)
  base = con.find(r'href=',target)
  end = con.find('>',base)
  i = i + 1
while j < 30:
    content = urllib.urlopen(url[j]).read()
    print url[0]
    open(r'zhihu/'+url[j],'w+').write(content)
    print 'downloading',
    j = j + 1
    time.sleep(15)  

#zhihu_download
#!/usr/bin/env python
import time
import urllib

i = 0
j = 0
url = ['']*30
name = ['']*30
con = urllib.urlopen('http://www.zhihu.com/collection/19668036').read()
target = con.find(r'<a target="_blank')
base = con.find(r'href=',target)
end = con.find('>',base)
url[0] = 'http://www.zhihu.com' + con[target +25 :end - 1]
#print url[0]


while target != -1 and base != -1 and end != -1 and i < 30:
  url[0] = 'http://www.zhihu.com' + con[target +25 :end - 1]
  name[0] =  con[base +16 :end - 1]
  target = con.find(r'<a target="_blank',end)
  base = con.find(r'href=',target)
  end = con.find('>',base)
  content = urllib.urlopen(url[0]).read()
  open(r'zhihu/'+name[0]+'.html','w+').write(content)
  print 'downloading',name[0]
  time.sleep(5)
  i = i + 1
  
  
#下载所有页面
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
	
#下载所有页面_改编	
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
else:
    print 'Download Over!'
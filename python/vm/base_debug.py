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


while target != -1 and base != -1 and end != -1 and	i < 30:
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

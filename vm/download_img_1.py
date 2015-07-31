#!/usr/bin/env python
import time
import urllib

i = 0
url = ['']*10
name = ['']*10
con = urllib.urlopen('http://www.ithome.com/html/bizhi/164396.htm').read()
src = con.find(r'/newsuploadfiles')
end = con.find(r'.jpg',src)
name[0] = con[src +24 :end +1]
while src != -1 and end != -1 and i < 10:
	url[0] = con[src -21 :end +4]
	src = con.find(r'/newsuploadfiles',end)
	end = con.find(r'.jpg',src)
	content = urllib.urlopen(url[0]).read()
	open(r'img/'+ name[0]+'jpg','w+').write(content)
	name[0] = con[src +24 :end +1]
	print url[0]
	time.sleep(3)
	i = i + 1
else:
	print "Download Over!"

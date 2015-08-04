import urllib2

i = 1
con = urllib2.urlopen('https://mm.taobao.com/json/request_top_list.htm?type=0&page=1').read()
mhref = con.find(r'<a href=')
mend = con.find(r'target=',mhref)
url = con[mhref +11 :mend -2]
while mhref != -1 and mend != -1 and i < 20:


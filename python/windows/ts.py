import urllib

url = 'http://weibo.com/u/2662140207/home?end_id=3871506746364928&pre_page=1&page=2'
cont = urllib.urlopen(url).read()
open(r'D:\\Document\\python\\tmp\\ts.html','w+').write(cont)

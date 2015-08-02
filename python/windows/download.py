import urllib
import urllib2

url = 'http://www.zhihu.com'
user_angent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0'
headers = { 'User-Agent' : user_angent }

requset = urllib2.Request(url,headers)
reponse = urllib2.urlopen(requset).read()
print reponse

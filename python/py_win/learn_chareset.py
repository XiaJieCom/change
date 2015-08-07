import urllib
import chardet
'''
#url = 'http://www.baidu.com'
url = 'http://www.iplaypython.com'
content = urllib.urlopen(url).read()
#print info.getparam('charset')
result =  chardet.detect(content)
print result['encoding']
'''

def automatic_detect(url):
    content = urllib.urlopen(url).read()
    result =  chardet.detect(content)
    encoding = result['encoding']
    return encoding

url = 'http://www.iplaypython.com'
print automatic_detect(url)


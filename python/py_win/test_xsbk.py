# coding:utf-8

import re
import random
import urllib
import urllib2
from bs4 import BeautifulSoup


url = 'http://www.qiushibaike.com'

my_headers = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
    'ELinks/0.12pre5 (textmode; Linux; -)'
]

def get_con(url,headers):
  random_header = random.choice(headers)
  print random_header
  req = urllib2.Request(url)
  req.add_header('User-Agent',random_header)
  req.add_header('Host','www.qiushibaike.com')
  req.add_header('Referer','http://blog.csdn.net/pleasecallmewhy/article/details/8932310')
  req.add_header('GET','url')
  content = urllib2.urlopen(req).read()
  return content
def get_txt(info):
    soup = BeautifulSoup(info)
    all_txt = soup.find_all('div',class_="content")
    print len(all_txt)
    for txt in all_txt:
        print txt

info = get_con(url,my_headers)
print get_txt(info)
'''

<div class="content">

xxxxx！
<!--2015-08-05 21:47:54-->

</div>
'''
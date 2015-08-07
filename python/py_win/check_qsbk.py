# coding:utf-8
import time
import random
import urllib2
from bs4 import BeautifulSoup

url = 'http://www.qiushibaike.com/text/page/'

my_headers = [
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    'ELinks/0.12pre5 (textmode; Linux; -)'
]


def get_con(url, headers):
    random_header = random.choice(headers)
    req = urllib2.Request(url)
    req.add_header('User-Agent', random_header)
    req.add_header('Host', 'www.qiushibaike.com')
    req.add_header(
        'Referer', 'http://www.qiushibaike.com/')
    req.add_header('GET', 'url')
    content = urllib2.urlopen(req).read()
    return content


def get_txt(haha):
    soup = BeautifulSoup(haha)
    all_txt = soup.find_all('div', class_="content")
    i = 1
    for txt in all_txt:
        cont = str(txt)
        head = cont.find(r'class="content"')
        end = cont.find(r'</div', head)
        con = cont[head + 16:end]
        print str(i), con
        i = i + 1
        time.sleep(3)
page = raw_input("Please input a number:")
p = int(page)
while p < 36:
  haha = get_con(url + str(p) + '?s=4796159', my_headers)
  print get_txt(haha)
  print "这是第" + str(p) + "页"
  p = p + 1
  
'''
<a href="/history/page/2?s=JMJJ9J6SGXDILL0T">2</a>
http://www.qiushibaike.com/history/page/3?s=JMJJ9J6SGXDILL0T
250
'''

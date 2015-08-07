# coding:utf-8
import random
import urllib2
from bs4 import BeautifulSoup

url = 'http://xiajie.blog.51cto.com'

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
    req.add_header('Host', 'xiajie.blog.51cto.com')
    req.add_header(
        'Referer', 'http://xiajie.blog.51cto.com/6044823/1682355')
    req.add_header('GET', 'url')
    content = urllib2.urlopen(req).read()
    return content

def get_txt(haha):
    soup = BeautifulSoup(haha)
    all_txt = soup.find_all('div', class_="modCon")
    for txt in all_txt:
        cont = str(txt)
        head = cont.find(r'xiajiesina')
        end = cont.find(r'<a href', head)
        con = cont[head:end]
        print con
p = 1
while p < 11:
    haha = get_con(url, my_headers)
    print get_txt(haha)
    print "这是第" + str(p) + "次"
    p = p + 1

'''
<div class="modCon">
<p>
<span class="infoListHead"></span>
用户名：xiajiesina
<br>
文章数：49
<br>
评论数：5
<br>
访问量：3474
<br>
<a target="_blank" href="http://home.51cto.com/index.php?s=/Account/credit">无忧币</a>
：415
<br>
<a target="_blank" href="http://51ctoblog.blog.51cto.com/26414/5591">博客积分</a>
：332
<br>
<a target="_blank" href="http://51ctoblog.blog.51cto.com/26414/5591">博客等级</a>
：3
<br>
注册日期：2012-09-20
<br>
<script src="http://blog.51cto.com/active/no1/blogno1countdown.php">
</p>
</div>
'''

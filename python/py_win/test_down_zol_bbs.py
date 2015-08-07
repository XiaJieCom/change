# coding:utf-8
import random
import urllib
import urllib2
from bs4 import BeautifulSoup

local = 'D:/Document/Linux/python/tmp/'
url = 'http://bbs.zol.com.cn/dcbbs/d16_94142.html#picIndex11'

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
    req.add_header('Host', 'bbs.zol.com.cn')
    req.add_header(
        'Referer', 'http://bbs.zol.com.cn/dcbbs/d16_94142.html')
    req.add_header('GET', 'url')
    content = urllib2.urlopen(req).read()
    return content

def get_txt(haha):
    soup = BeautifulSoup(haha)
    all_txt = soup.find_all('img', class_="lazy")
    for txt in all_txt:
    	
        cont = str(txt)
        head = cont.find(r'data-original')
        end = cont.find(r'data-picid', head)
        con = cont[head + 15:end -2]
        jpg_name = cont[head + 78:end -2]
        urllib.urlretrieve(con,local + jpg_name)
        print "Download ...",jpg_name

haha = get_con(url, my_headers)
print get_txt(haha)

'''
/dcbbs/d16_94203.html
a href="javascript:;">
<img class="lazy" width="1055" height="1559" data-info="1200#1" data-role="gallery" data-picid="36454715" data-original="http://i5.bbswater.fd.zol-img.com.cn/t_s1200x5000/g2/M00/06/03/ChMlWlXCsTaIeeoGAAu3ynw9fjsAAITDwNg_cIAC7fi305.jpg" data-width="1200" src="http://i5.bbswater.fd.zol-img.com.cn/t_s1200x5000/g2/M00/06/03/ChMlWlXCsTaIeeoGAAu3ynw9fjsAAITDwNg_cIAC7fi305.jpg" datasrc="g2/M00/06/03/ChMlWlXCsTaIeeoGAAu3ynw9fjsAAITDwNg_cIAC7fi305.jpg" style="border: 0px none; cursor: pointer; display: inline;" data-src="1">
</a>
'''

import urllib2

str0 = '<a href="/question/32456147" target="_blank">'
con = urllib2.urlopen('http://www.zhihu.com/collection/34392792').read()
print 'con',con

href = str0.find(r'href=')
end = str0.find(r'" target')
url = str0[href + 6:end]
base = 'http://www.zhihu.com'
print base + url
content = urllib2.urlopen(base + url).read()
f_name = url[10:]+'.html'
open(f_name,'w').write(content)
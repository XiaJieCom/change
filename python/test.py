import urllib
p = 1
base = "http://www.zhihu.com/collection/19668036?page="
while p < 2:
    page = base + str(p)
    print page
    p = int(p)
    p = p + 1
    con = urllib.urlopen(page).read()

    print con

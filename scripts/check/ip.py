__author__ = 'jack'
#!/usr/bin/env python
a = '10.0.0.'
with open('ip.txt','a+') as f:
    for i in range(255):
        f.write(a+str(i) + '\n' )


#!/usr/bin/env python

#list = ['a.txt','b.txt','c.txt']

#def read():
#	for i in list:
#	 return i
#print read()
import os
import os.path
rootdir = "/python/tmp"



for root,dirs,filenames in os.walk(rootdir):
 for filename in filenames:
  for line in open(root+os.sep+filename):
   print line,
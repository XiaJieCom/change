#!/bin/bash
ls -l >/tmp/list.log
file="/tmp/list.log"
lines=`cut -f1 |wc -l $file |grep -v total`
print $lines
for i in `seq 1 $lines`;do
year=`head -$i $file |tail -1|cut   -f6`
mon=`head -$i $file |tail -1|cut -d  -f7`
mv $i $year$mon'_'$i
done

#!/bin/bash
file=/etc/passwd
num=(20 40 60 56 32 25)
for ((i=0;i<${#num[*]};i++))
do
	head -${num[$i]} $file |tail -1 >>/tmp/test.log
done

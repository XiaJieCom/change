#!/bin/bash
cd /var
dir=($(ls -l |awk '{print $9}'))
for ((i=0;i<${#dir[*]};i++));do
echo "hello ${dir[$i]}"
done
echo ${#dir[*]}

#!/bin/bash
file=/etc/passwd
LINES=`cut -d ":" -f1 $file |wc -l`
for i in `seq 1 $LINES`;do
id=`head -$i $file | tail -1 |cut -d ":" -f3`
name=`head -$i $file | tail -1 |cut -d ":" -f1`
echo "hello $name,your UID is $id"
done
echo $LINES


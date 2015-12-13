#!/bin/bash
list=(1 2 3)
for ((i=0;i<${#list[*]};i++))
do
	echo $[${list[$i]}*$1]
done

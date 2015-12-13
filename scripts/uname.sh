#!/bin/bash
#iplist=(192.168.1.104 127.0.0.1)
iplist=(127.0.0.1)
for ((i=0;i<${#iplist[*]};i++))
do
	ssh jack@${iplist[$i]} "uname -a"
done

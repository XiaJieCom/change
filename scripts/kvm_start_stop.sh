#!/bin/bash
host=($(virsh list --all |grep -v "Name\|kvm-demo"|awk '{print $2}'))
while true
do
	virsh list --all
	echo -e " Start   all servers! 1)\n Stop    all servers! 2)\n Suspend all servers! 3)\n Resume  all servers! 4)"
	read -p "Please input your choice: " choice
	case $choice in
	1) echo "Start all machine ...";sleep 3
		for ((i=0;i<${#host[*]};i++))
		do
			virsh start "${host[$i]}"
		done
		clear
		virsh list --all
		break
		;;
	2) echo "Stop all machine ...";sleep 3
		for ((i=0;i<${#host[*]};i++))
		do
			virsh destroy "${host[$i]}"
		done
		clear
		virsh list --all
		break
		;;
	3) echo "Suspend all machine ...";sleep 3
		for ((i=0;i<${#host[*]};i++))
		do
			virsh suspend "${host[$i]}"
		done
		clear
		virsh list --all
		break
		;;
	4) echo "Resume all machine ...";sleep 3
		for ((i=0;i<${#host[*]};i++))
		do
			virsh resume "${host[$i]}"
		done
		clear
		virsh list --all
		break
		;;
	esac
done


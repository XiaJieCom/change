#!/bin/bash
host=($(virsh list --all |grep -v "Name"|awk '{print $1}'))
while true
do
	virsh list --all
	read -p "Please input your choice: " choice
	case $choice in
	1) echo "Start all machine ...";sleep 3
		for ((i=0;i<${#host[*]};i++))
		do
			virsh start "${host[$i]}"
		done
		virsh list --all
		break
		;;
	2) echo "Stop all machine ...";sleep 3
		for ((i=0;i<${#host[*]};i++))
		do
			virsh destroy "${host[$i]}"
		done
		virsh list --all
		break
		;;
	3) echo "Suspend all machine ...";sleep 3
		for ((i=0;i<${#host[*]};i++))
		do
			virsh suspend "${host[$i]}"
		done
		virsh list --all
		break
		;;
	4) echo "Resumed all machine ...";sleep 3
		for ((i=0;i<${#host[*]};i++))
		do
			virsh resumed "${host[$i]}"
		done
		virsh list --all
		break
		;;
	esac
done


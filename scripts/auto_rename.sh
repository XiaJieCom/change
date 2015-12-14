#!/bin/bash
fname=($(ls -lth |head -2 |grep -v "total" |awk '{print $9}'))
year=($(ls -lth |head -2 |grep -v "total" |awk '{print $6}'))
mon=($(ls -lth |head -2 |grep -v "total" |awk '{print $7}'))
mv $fname $year$mon'_'$fname
clear
ls -l

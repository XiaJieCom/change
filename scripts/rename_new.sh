#!/bin/bash
fname=$1
year=($(ls -ls $1 |awk '{print $7}'))
mon=($(ls -ls $1 |awk '{print $8}'))
mv $fname $year$mon'_'$fname
echo `ls -l $year$mon'_'$fname`

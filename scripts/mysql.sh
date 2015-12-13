#!/bin/bash
master1=192.168.1.12
slave1=192.168.1.14
port=3306
status=$(/mysql -uslave -p123 -h $master1 "show slave status \G"|grep -i "running")
IO_env=`echo $status |grep IO |awk '{print $2}'`
SQL_env=`echo $status |grep SQL |awk '{print $2}'`
DATE=`date +"%y-%m-%d %H:%M:%s"`
if [$port == 3306]
then
	echo "mysql is running..."
else
	echo "Warn !$master1 mysql id down" 13121889803@163.com
fi
if ["$IO_env" == "Yes" -a "$SQL_env" == "Yes"]
then
	echo "Slave is ok ..."
else
	echo "#####################$date##########" >>/tmp/mysql_check_slave.log
	echo "Slave is not running!" >>/tmp/mysql_check_slave.log
	echo "Slave is not running!" |mail -s "Warn!$slave1 mysql slave is not running"13121889803@163.com
fi

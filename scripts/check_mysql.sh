#!/bin/bash
master1=192.168.1.12
slave1=192.168.1.14
slave2=192.168.1.15
host=($slave1 $slave2)
DATE=`date +"%Y-%m-%d %H:%M:%S"`
echo "Check all of mysql slave status "
for ((i=0;i<${#host[*]};i++))
do
    status=$(mysql -umysql_check -p123 -h ${host[$i]} -e "show slave status \G"|grep -i "running")
    IO_env=`echo $status  |grep IO |awk '{print $2}'`
    SQL_env=`echo $status |grep SQL |awk '{print $2}'`
    if [ "$IO_env" == "Yes" -a "$SQL_env" == "Yes" ]
    then
        echo "${host[$i]} is ok ..."
    else
        echo "#####################$date##########" >>/tmp/mysql_check_slave.log
        echo "$DATE     ${host[$i]}     is not ok!" >>/tmp/mysql_check_slave.log
        echo "$DATE     ${host[$i]}     is not ok!" |mail -s "Warn!$slave1 mysql slave is not ok" -r mysql_check@localhost.com 13121889803@163.com
    fi
done

#使用该脚本之前需要先对数据库进行如下操作

#create user 'mysql_check'@'%' identified by '123';
#flush privileges;
#grant SUPER,REPLICATION CLIENT on *.*  to 'mysql_check'@'%';
#flush privileges;
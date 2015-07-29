#!/bin/bash
DATE=`date +%F`
CLEAR=`date -d "10 days ago" +%F`
MYSQL='/usr/local/mysql/bin/mysqldump --opt '
WEBSITEDIR=/home/www-data/public_html
MYSQLDATA=/usr/local/mysql/data
DBBACKDIR=/backup/daily/mysql
WEBBACKDIR=/backup/daily/web

#web site backup
cd $WEBSITEDIR
for web in `ls`
do
        tar zcf $WEBBACKDIR/$web-$DATE.tar.gz $web
done

cd -

#mysqldump db
for db in `find /usr/local/mysql/data -type d  |sed 's#/usr/local/mysql/data/##g' |grep -v "\/" |grep -v performance_schema`
do
        $MYSQL  $db >$DBBACKDIR/$db-$DATE.sql
done

#clear
cd $DBBACKDIR
ls |grep $CLEAR |xargs rm -f
cd $WEBBACKDIR
ls |grep $CLEAR |xargs rm -f
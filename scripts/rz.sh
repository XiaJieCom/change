#!/bin/bash 
#currentdate=`date +%Y%m%d%H%M`
host=192.168.100.182
src=/rsync/web/
des=web
user=root




/usr/local/bin/inotifywait -mrq --timefmt '%d/%m/%y %H:%M' --format '%T %w%f%e' -e modify,delete,create,attrib $src | while read files 

do 
currentdate=`date +%Y%m%d%H%M`
mkdir /rsync/back/$currentdate
cd /rsync
tar -zcvf /rsync/back/$currentdate/back.tar.gz ./web
/usr/bin/rsync -vzrtopg --delete --progress --password-file=/etc/rsyncd.passwd $src $user@$host::$des 

echo "${files} was rsynced" >>/rsync/rsync.log 2>&1 
done


#!/bin/bash 

host=192.168.200.17
src=/file/nwww/
des=nwww
user=root


/usr/local/bin/inotifywait -mrq --timefmt '%d/%m/%y %H:%M' --format '%T %w%f%e' -e modify,delete,create,attrib /file/nwww/SCMHost/Bin | while read files 

do

#rsync dir


/usr/bin/rsync -vzrtopg  --progress  --exclude=*.tar.gz --exclude=.svn --exclude=/file/nwww/AccountHost/Bin/log  "$src"AccountHost/Bin $user@$host::"$des"/AccountHost/Bin/
/usr/bin/rsync -vzrtopg  --progress  --exclude=*.tar.gz --exclude=.svn --exclude=/file/nwww/SCMHost/Bin/log      "$src"SCMHost/Bin/ $user@$host::"$des"/SCMHost/Bin/
/usr/bin/rsync -vzrtopg  --progress  --exclude=*.tar.gz --exclude=.svn --exclude=/file/nwww/WebHost/Bin/log      "$src"WebHost/Bin/ $user@$host::"$des"/WebHost/Bin/

# restart apache 

/etc/init.d/httpd restart
sh root@192.168.200.17 "/etc/init.d/httpd restart"



echo "${files} was rsynced" >>/scripts/web_rsync.log 2>&1
done
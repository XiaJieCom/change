IDC
37	db

GZ
6	db




57.web-salve:
    */5 * * * * /usr/sbin/ntpdate 192.168.100.61  >> /var/log/ntp.log && /sbin/hwclock -w
60.demo:
    */5 * * * * /usr/sbin/ntpdate 192.168.100.61  >> /var/log/ntp.log && /sbin/hwclock -w
    0 3 * * 1 /file/bak/backup.sh >> /file/bak/backup.log 2>&1
55.demo1:
    */5 * * * * /usr/sbin/ntpdate 192.168.100.61  >> /var/log/ntp.log && /sbin/hwclock -w
    */5 * * * * /root/sh/check_http.sh >> /root/sh/check.log 2>&1
56.web-master:
    */5 * * * * /usr/sbin/ntpdate 192.168.100.61  >> /var/log/ntp.log && /sbin/hwclock -w
    0 2 * * * /file/httpdlog/dellog.sh >> /file/httpdlog/dellog.log 2>&1
54.app:
    */5 * * * * /usr/sbin/ntpdate 192.168.100.61  >> /var/log/ntp.log && /sbin/hwclock -w
61.monitor:
    */1 * * * * /usr/bin/php /var/www/html/cacti/poller.php &> /dev/null
    */5 * * * * /usr/sbin/ntpdate 0.cn.pool.ntp.org >> /var/log/ntp.log
    30 23 * * * /usr/local/smokeping/smokeping_restart.sh
    0 8 * * * /srv/salt/check.sh
20.demo1db:
    40 0 * * * /file/bak/backup_new_5432_update1.sh>/tmp/backup_log.log 2>&1
    20 0 * * * /file/pgsql9.1/pg_log/deletelog.sh
    0 3 * * * /usr/sbin/ntpdate 192.168.100.61  >> /var/log/ntp.log && /sbin/hwclock -w
52.mail:
    0 6  * * * /usr/sbin/ntpdate 192.168.100.61 >> /var/log/ntp.log 2>&1 && /sbin/hwclock -w
    0 0 * * * sh -x /home/zc/maillog_everyday.sh > /var/log/mailrota.log 2>&1
37.dbslave:
    */5 * * * * /usr/sbin/ntpdate 192.168.100.61  >> /var/log/ntp.log
    20 0 * * * /file/cyberdata/pg_log/deletelog.sh
    10 3 * * * /file/dbbak/crontabback.sh >> /file/dbbak/crontabback.log 2>&1
 51.dbmaster:
    */5 * * * * /usr/sbin/ntpdate 192.168.100.61  >> /var/log/ntp.log 2>&1

GZ

11.report:
    */5 * * * * /usr/sbin/ntpdate 192.168.200.7 >> /var/log/ntp.log 2>&1
14.db2:
    */5 * * * * /usr/sbin/ntpdate 192.168.200.7 >> /var/log/ntp.log 2>&1
16.demo-dbmaster:
    0 2 * * * /usr/sbin/ntpdate 192.168.200.7 >> /var/log/ntp.log 2>&1
13.db1:
    */5 * * * * /usr/sbin/ntpdate 192.168.200.7 >> /var/log/ntp.log 2>&1
17.web2:
    */5 * * * * /usr/sbin/ntpdate 192.168.200.7 >> /var/log/ntp.log 2>&1
9.ermweb1:
    */5 * * * * /usr/sbin/ntpdate 192.168.200.7 >> /var/log/ntp.log 2>&1
15.demo-erm:
    0 2 * * * /usr/sbin/ntpdate 192.168.200.7 >> /var/log/ntp.log 2>&1
12.mq:
    */5 * * * * /usr/sbin/ntpdate 192.168.200.7 >> /var/log/ntp.log 2>&1
7.nginx1:
    55 23 * * * sh -x /usr/local/nginx/lognginx.sh > /var/log/nginx.log 2>&1
6.ermapp:
    */5 * * * * /usr/sbin/ntpdate 192.168.200.7 >> /var/log/ntp.log 2>&1
    30 2 * * * /data/dbback/databaseback.sh >> /data/dbback/databaseback.log 2>&1
    30 3 * * * /data/dbback/datademoback.sh >> /data/dbback/demobak/datademoback.log 2>&1
8.nginx2:
    */5 * * * * /usr/sbin/ntpdate 192.168.200.7 >> /var/log/ntp.log 2>&1
    55 23 * * * sh -x /usr/local/nginx/lognginx.sh > /var/log/nginx.log 2>&1
    30 23 * * * /usr/local/smokeping/smokeping_restart.sh
    0 8 * * * /scripts/check.sh
10.web1:
    */5 * * * * /usr/sbin/ntpdate 192.168.200.7 >> /var/log/ntp.log 2>&1
    #*/3 * * * * /usr/src/res.sh	
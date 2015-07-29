
http://www.centoscn.com/IT/2015/0705/5805.html  大型网站图片服务器架构的演进

http://www.centoscn.com/IT/2015/0705/5806.html  大型Web系统架构


http://blog.csdn.net/longeremmy/article/details/8012532  http 报文详解

查找出20天之前的创建的文件，并且列出或者删除
	备注：在使用的时候出现一些问题，比如不能直接列出希望看到的目录
	find /backup/ -type f  |grep `date -d  "20 days ago" +%Y-%m-%d` |xargs rm -f
	find . -type f |grep `date -d "30 days ago" +%Y-%m-%d` |xargs ls -l

date 命令
	date -d last-month

查找出某一天的文件，并且列出或者删除
	find /backup/ -type f  |grep "2013-12-13" | xargs ls -l
	find . -type f  |grep "2014-03" | xargs ls -l
	find . -type f  |grep "2014-03" | xargs ls -l
	find ../ -type f |grep `date -d "29 days ago" +%Y-%m-%d` |xargs rm -rf
查找出创建于31天之前的文件，列出或者删除
	find /backup/ -type f -ctime 31 |xargs ls -l
	find /backup/ -type f -ctime 31 |xargs rm -f
	
对于其它端口的scp传输
scp -r -P3389 maldetect-1.4.2 root@218.246.35.234:/root/


find /backup/ -type f  |grep "2014-0101" | xargs ls -l
find ../ -type f  |grep "2014-04" | xargs ls -l
find . -type f  |grep "2013-" | xargs rm -rf

解决libmysqlclient.so.16: cannot open shared object file: No such file or directory failed问题
 ln -s /usr/local/mysql/lib/libmysqlclient.so.16 /usr/lib/

grep -R "88683" /var/www/wip.gjjx.com.cn | xargs ls -l


 mysqldump -u yncy --opt  > /backup/daily/mysql/yncy-2014-04-20.sql
 杀死yum
 ps -elf|grep yum|grep -v grep|awk '{print $4}'|xargs kill -9
 
 ./configure --with-oci8=instantclient,/usr/lib/oracle/10.2.0.5/client/lib/ --with-php-config=/usr/local/php/bin/php-config
 
   mysqldump -uroot -p  wip_com  -e --max_allowed_packet=1048576 --net_buffer_length=16384 > wip_com.sql
 
 
 grant all on  wp.* to wp@localhst identified by "wp";
 grant all on  web.* to web@% identified by "'R0od0owP";
 
 mysql 数据库导出
 /usr/local/mysql/bin/mysqldump  -uroot   -p  wip  -l   -F  > /tmp/test.sql 

 
 grant all privileges on www_jincheng.* to 'Chiw'@'172.20.72.11' identified by "BnLDmFn9ZXTIk";
 
 grant all privileges on wip.* to 'ievaeM7u'@'192.168.86.50/24' identified by "n1MMMrSPIgWdw";
 
 
 替换
 update `wip_category' SET `url` = replace(url, 'pzh96196.xiuqi.org', '');
 
 update `wip_users` SET `name` = replace(username, 'vungu', 'jcnews');
 
  
 /usr/local/pgsql/bin/psql  newsuncoo_demo -U newsuncoo  -W1!newsuncoo
 
 
 JDK  http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#!/bin/bash
#已经得知域名目录，希望增加一个新的FTP账号和密码
#user  
#password
#webdir
#pwddir
#binfile
#profiledir
USERNAME=`mkpasswd -l 10 -d 2 -C 5 -s 0`
PASSWORD=`mkpasswd -l 16 -d 3 -C 5 -s 2`
WEBDIR=/home/www-data/public_html
PWDFILE=/etc/vsftpd/logins.txt
BINFILE=/etc/vsftpd/login.db
PROFILEDIR=/etc/vsftpd/conf

read -p "Insert Domain Name : " DM
echo "######################"
echo "Domain Name is : $DM "
echo -n "FTP port : " & netstat -ntlp|grep vsftpd|awk '{print $4}'|awk -F ':' '{print $2}'
echo "FTP User is : $USERNAME "
echo "FTP Password is : $PASSWORD "
cd $WEBDIR/$DM
echo "Website is : $WEBDIR/$DM "
echo $USERNAME >> $PWDFILE
echo $PASSWORD >> $PWDFILE
#把创建的用户写入vsftpd/conf/用户配置中，而且只能访问自己的目录
echo "write_enable=YES" >> $PROFILEDIR/$USERNAME
echo "anon_world_readable_only=NO" >> $PROFILEDIR/$USERNAME
echo "anon_upload_enable=YES" >> $PROFILEDIR/$USERNAME
echo "anon_mkdir_write_enable=YES" >> $PROFILEDIR/$USERNAME
echo "anon_other_write_enable=YES" >> $PROFILEDIR/$USERNAME
echo "local_root=/home/www-data/public_html/$DM" >> $PROFILEDIR/$USERNAME
#加密
db_load -T -t hash -f /etc/vsftpd/logins.txt /etc/vsftpd/login.db
#重启vsftpd
/etc/init.d/vsftpd restart
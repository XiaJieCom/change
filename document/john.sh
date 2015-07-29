一、下载john  (官方网站http://www.openwall.com/john/)

wget http://www.openwall.com/john/j/john-1.8.0-jumbo-1.tar.xz


	yum install xz -y
	
    $xz -d ***.tar.xz

    $tar -xvf  ***.tar

二、安装并利用john破解密码

[root@Centosliang run]# tar xzvf john-1.7.6.tar.gz

[root@Centosliang run]# cd john-1.7.6

[root@Centosliang run]# cd src/

[root@Centosliang run]# ./configure

[root@Centosliang run]# make


[root@Centosliang run]# cd ../run

[root@Centosliang run]# cp /etc/passwd /etc/shadow .


[root@Centosliang run]# ./unshadow passwd shadow >mypasswd

[root@Centosliang run]# ./john mypasswd
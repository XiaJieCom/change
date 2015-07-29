一、安装基本的lamp环境

yum install httpd subversion mod_dav_svn mysql-server php php-mbstring -y

#创建svn 的数据库
    mysql -u root -p
      
    mysql> CREATE DATABASE svnmanager;  
    mysql> GRANT all privileges on svnmanager.* to 'svnmanager'@'localhost' identified by 'XXX';  
    mysql> FLUSH PRIVILEGES;  
    mysql> exit  

#安装Pear模块：VersionControl_SVN 
pear install PEAR-1.9.4
pear install VersionControl_SVN-0.3.4 



二、配置基本的svn

mkdir -pv /svn/repos

vim /etc/httpd/conf/httpd.conf

增加以下配置
#/svn/accessfile 访问控制文件
#/svn/passwdfie  密码文件


<Location /svn>
   DAV svn
   SVNParentPath /svn
   AuthType Basic
   AuthName "Authorization SVN"
   AuthzSVNAccessFile /svn/accessfile
    AuthUserFile /svn/passwdfile
    Require valid-user
</Location>

三、安装svnmanager

cd /usr/src
wget http://prdownloads.sourceforge.net/svnmanager/svnmanager-1.10.tar.gz
tar -zxvf svnmanager-1.10.tar.gz
mv svnmanager-1.10 /var/www/html
cd /var/www/html 
cp config.php.linux config.php

vim config.php
#修改配置文件

$svn_config_dir             =   "/svn/repos";
$svn_repos_loc              =   "/svn/repos";
$svn_passwd_file            =   "/svn/passwdfile";
$svn_access_file            =   "/svn/accessfile";

$dsn                =   "mysqli://svnmanager:svnmanager@localhost/svnmanager";



登录 http://localhost/svnmanager  
验证OK！

四、常见错误

1、PHP Fatal error:  Call to undefined function mb_internal_encoding() in /var/www/html/svnmanager/svnmanager/MainModule/DataModule.php on line 19

原因：没有安装mbstring 扩展
解决：yum install php-mbstring -y

2、提示VersionControl_SVN找不到

原因：没有安装VersionControl_SVN 该模块
解决：pear install PEAR-1.9.4
	  pear install VersionControl_SVN-0.3.4 
	  
3、页面空白

原因：1、数据库连接错误，可能没有安装mysqli扩展

解决：$dsn                =   "mysql://svnmanager:svnmanager@localhost/svnmanager";

1.下载安装源码包：
httpd-2.2.23.tar.gz php-5.3.19.tar.gz  mono-2.2.tar.bz2 mod_mono-2.2.tar.bz2 xsp-2.2.tar.bz2 （按此顺序安装）

前期准备:
yum install -y gcc gcc-c++ autoconf libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel libxml2 libxml2-devel zlib zlib-devel glibc glibc-devel glib2 glib2-devel bzip2 bzip2-devel ncurses ncurses-devel curl curl-devel e2fsprogs e2fsprogs-devel krb5 krb5-devel libidn libidn-devel openssl openssl-devel openldap openldap-devel nss_ldap openldap-clients openldap-servers bison* glib* flex readline readline-devel apr apr-util apr-devel

(yum安装：yum -y install httpd httpd-devel php-mbstring php php-devel)

---------------
要求图片生成功能:
yum install bison pkgconfig gettext make libtiff-devel libexif-devel giflib-devel libX11-devel fontconfig-devel cairo-devel

安装 libgdiplus

 wget http://download.mono-project.com/sources/libgdiplus/libgdiplus-2.10.tar.bz2
 wget http://download.mono-project.com/sources/libgdiplus/libgdiplus-3.8.tar.gz
 tar -jxvf libgdiplus-3.8.tar.gz
 cd libgdiplus-3.8
 ./configure
 make
 make install
 echo "/usr/local/lib" > /etc/ld.so.conf.d/mono.conf
 ldconfig 
-----------------------------

2.安装apache:
tar zxf httpd-2.2.23.tar.gz
cd httpd-2.2.23
./configure --prefix=/usr/local/apache2 --enable-module=so  --enable-rewrite=shared  (--with-mpm=worker) --with-mpm=prefork
make
make install
useradd apache -M -s /sbin/nologin
修改httpd.conf 启动用户和组改成apache
修改程序目录为 /file/www

3.安装php：（需要启用PHP压缩，php rewrite）
tar zxf php-5.3.19.tar.gz
cd php-5.3.19
./configure --prefix=/usr/local/php5 --with-apxs2=/usr/local/apache2/bin/apxs --enable-zip
make
make install
cp php.ini-production /usr/local/php5/php.ini
修改httpd.conf:
DirectoryIndex index.html index.php
添加此行: AddType application/x-httpd-php .php

4.安装mono：
tar jxvf mono-3.10.0.tar.bz2
cd mono-3.10.0
./configure --prefix=/usr/local/mono
make
make install
修改/etc/porfile在最后面添加：(一定要在编译mod_mono前生效，编译mod_mono需要用)
PKG_CONFIG_PATH=/usr/local/mono/lib/pkgconfig
export PKG_CONFIG_PATH
PATH=/usr/local/mono/bin:$PATH
export PATH

PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
export PKG_CONFIG_PATH
PATH=/usr/local/bin:$PATH
export PATH

运行 source /etc/profile

mkdir -p /usr/share/.mono/keypairs

tar jxf mod_mono-2.2.tar.bz2
cd mod_mono-2.2
./configure --prefix=/usr/local/mono
make
make install

tar jxf xsp-2.2.tar.bz2
cd xsp-2.2
./configure --prefix=/usr/local/mono
 make
 make install

将测试文件从/usr/local/mono/lib/xsp/test 拷贝到/file/www下：
  cp -R ../mono/lib/xsp/test/ /file/www/
修改httpd.conf，添加以下两行：
Include /usr/local/apache2/conf/mod_mono.conf
Include /etc/httpd/conf/mod_mono.conf
Alias /test "/file/www/test"
重启apache

修改/etc/porfile在最后面添加：
export LD_LIBRARY_PATH=/usr/local/mono/lib/:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/lib/:$LD_LIBRARY_PATH

---------------------
安装mod_mono2.4报错解决:
http://sjwt.vicp.cc:8080/post-287.html?archive=all
http://www.gzayong.info/ws/archives/223
https://trac.macports.org/ticket/28850

--------------
安装mod_mono2.8,须安装sqlite3.5以上版本：
tar zxvf sqlite-autoconf-3071501.tar.gz
./configure --prefix=/usr/local/sqlite3
export LD_LIBRARY_PATH=/usr/local/sqlite3/lib
-----------
安装postgresql：
./configure --prefix=/usr/local/pgsql9.1
gmake
gmake install
cd contrib/
make
make install
adduser postgres
mkdir /usr/local/pgsql/data
chown postgres /usr/local/pgsql/data
su - postgres
/usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data
创建日志目录 pg_log 修改配置文件 启动日志，并修改日志类型和输出格式
/usr/local/pgsql/bin/pg_ctl -D /usr/local/pgsql/data start


安装插件：
到pgsql安装目录:
cd /file/software/postgresql-9.1.2/contrib
make
make install

cd /file/software/postgresql-9.1.2/contrib/tablefunc
/usr/local/pgsql9.1/bin/psql -U postgres postgres < tablefunc--1.0.sql
/usr/local/pgsql9.1/bin/psql -U postgres b2b库 < tablefunc--1.0.sql




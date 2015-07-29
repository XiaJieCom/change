                  Mono详细配置
说明：如果使用mono最好安装linux图形界面。
系统：CentOS 5.3  32位 gnome图形界面
一．	下载软件
http://ftp.novell.com/pub/mono/sources/mod_mono/mod_mono-2.2.tar.bz2
http://ftp.novell.com/pub/mono/sources/xsp/xsp-2.2.tar.bz2
http://ftp.novell.com/pub/mono/sources/mono/mono-2.2.tar.bz2
共需下载三个软件：mono、mono_mod、xsp
二．	安装依赖的软件包
假设在mono检查系统环境期间如果提示“bosion package not found”，我们可以在命令行下用命令：
yum install bison*
完成对bison包的安装；
yum -y install groupinstall "Development Tools"
yum -y install httpd-devel*
yum install glib*
其他包安装过程同上。
三．	解开压缩包
先安装解压包：
tar jxvf mono-2.2.tar.bz2
tar jxvf mod_mono-2.2.tar.bz2
tar jxvf xsp-2.2.tar.bz2
四．	编译mono
进入到解压后的mono-2.2文件目录下执行以下命令
./configure
make && make install
（编译过程需要时间比较长，需要耐心等候）
以上安装为mono的基本配置。如需更进一步配置的加上mono编译参数。
六．	编译mod_mono
在解压后mod_mono-2.2文件目录下执行以下命令
./configure
make && make install
七．	编译xsp
安装xsp先设置环境变量：
vi  /etc/profile
添加：PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
export PKG_CONFIG_PATH
注意：lib库跟系统位数一致
     保存后执行以下命令:
						source /etc/profile
  echo $PKG_CONFIG_PATH 查看环境变量（有下面一行配置正确）
/usr/local/lib/pkgconfig
在解压后xsp-2.2文件目录下执行以下命令
./configure
make && make install
八．	配置apache
   vi /etc/httpd/conf/httpd.conf
在httpd.conf中加入：
Include /etc/httpd/conf/mod_mono.conf
Alias /test "/usr/local/lib/xsp/test"
重新启动apache进行测试
service httpd restart
打开IE进行测试，地址是: http://localhost/test/index.aspx
（localhost 是配置mono环境的ip地址）



PostgreSQL 
下载 postgresql-8.0.12.tar.gz ，放在 /opt/ 下面，接着运行 #tar –xvf postgresql-8.0.12.tar.gz 解压缩，进入 postgresql-8.0.12 目录，编译并安装： 
# ./configure --without-readline --without-zlib 
#make 
#make install 
进入安装好的目录， /usr/local/pgsql/ 创建数据库文件夹 #mkdir data ，接着在 CentOS 中创建新用户 postgres ，并授权 #chown postgres data ， #su postgres 切换到 postgres 用户下。

为其配置环境变量：
vim ~postgres/.bash_profile

PGLIB=/usr/local/pgsql/lib
PGDATA=$HOME/data
PATH=$PATH:/usr/local/pgsql/bin
export PGHOME=/usr/local/pgsql
export PGDATA=~/data
export PATH=$PATH:$HOME/bin:$PGHOME/bin
MANPATH=$MANPATH:/usr/local/pgsql/man
export PGLIB PGDATA PATH MANPATH 

初始化数据库： 
#./initdb -D /usr/local/pgsql/data 
最后到 /usr/local/pgsql/bin/ 下启动数据库 
#./ pg_ctl -D /usr/local/pgsql/data start

以后台方式启动postgre数据库服务
　　$ postmaster -i -D ~/data &
　　[1] 22603
　　[postgre@www postgre]$ DEBUG: Data Base System is starting up at Thu Jan 31 02:00:44 2002
　　DEBUG: Data Base System was shut down at Thu Jan 31 01:57:58 2002
　　DEBUG: Data Base System is in production state at Thu Jan 31 02:00:44 2002

　　这样 PostgreSQL 使用位于 /usr/local/pgsql/data 的数据库，允许 Internet 用户的连接（ -i ） ，并在后台运行。

且慢，数据库倒是启动了，但是通过客户端始终连接不上去，这是因为数据库监听端口还没打开，进入 /usr/local/pgsql/data/ 目录，找到 postgresql.conf 文件，把监听地址 listen_addresses = '*' 和监听端口 port = 5432 前面的 # 号注释去掉。做了这些还不够，还是报拒绝访问，在当前目录下找到 pg_hba.conf 文件，在该文件的下边找到 # IPv4 local connections 文字，把下面的参数改为 host    all         all         192.168.1.0/24             trust ，具体含义可以参考 postgres 官方配置文档。稍微解释解释一下，含义为在 192.168.1.0-192.168.1.255 之间的 ip 地址都可以访问数据库


创建数据库dm
$ ./createdb dm
   CREATE DATABASE


创建用户
$ ./createuser -A -D -E -P dm
   Enter password for new role: 123456
   Enter it again: 123456
   Shall the new role be allowed to create more new roles? (y/n) y
   CREATE ROLE
使用psql
$ ./psql -d dm -U dm
   Welcome to psql 8.2.4, the PostgreSQL interactive terminal.
   Type:   \copyright for distribution terms
        \h for help with SQL commands
        \? for help with psql commands
        \g or terminate with semicolon to execute query
        \q to quit
   dm=> \q

创建数据库
./createdb database dadb
\l   查看
删除数据库
./dropdb database dadb
  

连接数据库
./psql dadb –U postgres


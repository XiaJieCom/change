PostgreSQL 
下载 postgresql-9.2.1.tar.bz2 
http://download.chinaunix.net/down.php?id=25143&ResourceID=39&site=1
1、编译安装
tar –jxvf postgresql-9.2.1.tar.bz2 
cd postgresql-9.2.1
./configure --without-readline --without-zlib 
make 
make install 

2、新建用户，授权
创建数据库文件夹 #mkdir data
mkdir /usr/local/pgsql/data

创建新用户 postgres ，并授权 
useradd postgres
chown postgres.postgres /usr/local/pgsql/data

3、配置环境变量
切换到 postgres 用户
su postgres 

为其配置环境变量：
vim ~postgres/.bash_profile

PGLIB=/usr/local/pgsql/lib
PGDATA=$HOME/data
PATH=$PATH:/usr/local/pgsql/bin
MANPATH=$MANPATH:/usr/local/pgsql/man
export PGLIB PGDATA PATH MANPATH
export PGDATA=/usr/local/pgsql/data

4、初始化数据库并启动
#./initdb -D /usr/local/pgsql/data 
最后到 /usr/local/pgsql/bin/ 下启动数据库 
#./pg_ctl -D /usr/local/pgsql/data start

以后台方式启动postgre数据库服务
$ postmaster -i -D ~/data &
[1] 22603
[postgre@www postgre]$ DEBUG: Data Base System is starting up at Thu Jan 31 02:00:44 2002
DEBUG: Data Base System was shut down at Thu Jan 31 01:57:58 2002
DEBUG: Data Base System is in production state at Thu Jan 31 02:00:44 2002

这样 PostgreSQL 使用位于 /usr/local/pgsql/data 的数据库，允许 Internet 用户的连接（ -i ） ，并在后台运行。

5、更改监听端口，允许其它主机访问
且慢，数据库倒是启动了，但是通过客户端始终连接不上去，这是因为数据库监听端口还没打开。
vim /usr/local/pgsql/data/postgresql.conf 
把监听地址 listen_addresses = '*' 和监听端口 port = 5432 前面的 # 号注释去掉。

还是报拒绝访问，在当前目录下找到 pg_hba.conf # IPv4 local connections 
参数改为 
host    all         all     192.168.1.0/24     trust 
具体含义可以参考 postgres 官方配置文档。稍微解释解释一下，含义为在 192.168.1.0-192.168.1.255 之间的 ip 地址都可以访问数据库

host    all         all         203.187.177.130/24  trust #允许某个IP访问
host    all         all         0.0.0.0/0          trust  #允许所有IP访问

6、加入开机启动

cp /usr/src/postgresql-9.2.1/contrib/start-scripts/linux /etc/init.d/postgresql

chmod a+x /etc/init.d/postgresql

chkconfig --add postgresql






常见错误

pg_ctl等指令提示：

pg_ctl: no database directory specified and environment variable PGDATA unset

需要设置环境变量：

export PGDATA=/usr/local/pgsql/data



创建数据库dm
$ ./createdb dm
   CREATE DATABASE


创建用户
$ ./createuser -A -D -E -P dm0
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


select pg_start_backup('/usr/local/pgsql/data');

select pg_stop_backup();
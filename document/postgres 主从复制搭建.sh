1、编译安装
yum install -y gcc gcc-c++ automake autoconf libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel libxml2 libxml2-devel zlib zlib-devel glibc glibc-devel glib2 glib2-devel bzip2 bzip2-devel ncurses ncurses-devel curl curl-devel e2fsprogs e2fsprogs-devel krb5 krb5-devel libidn libidn-devel openssl openssl-devel openldap openldap-devel nss_ldap openldap-clients openldap-servers bison* glib* flex readline readline-devel apr apr-util apr-develrzsz sysstat e4fsprogs ntp readline-devel  openssl openssl-devel pam-devel libxml2-devel libxslt-devel python-devel tcl-devel  flex bison
tar –jxvf postgresql-9.2.1.tar.bz2 
cd postgresql-9.2.1
./configure  --prefix=/usr/local/pgsql 
gmake world
gmake install-world

2、新建用户，授权

创建数据库目录 
mkdir /data

创建用户 postgres ，并授权 

useradd postgres
chown postgres.postgres /data

3、配置环境变量

切换到 postgres 用户
su postgres 

为其配置环境变量：
vim ~postgres/.bash_profile

PGLIB=/usr/local/pgsql/lib
PGDATA=/data
PATH=$PATH:/usr/local/pgsql/bin
MANPATH=$MANPATH:/usr/local/pgsql/man
export PGLIB PGDATA PATH MANPATH
export PGDATA=/data

4、初始化数据库

initdb -D $PGDATA

5、Master 配置文件修改


vim pg_hba.conf

host    all             all               192.168.2.4/32          trust

host    all		        postgres          192.168.2.4/32          trust



vim postgres.conf

listen_addresses='*'

wal_level = 'hot_standby'

max_wal_senders = 3

wal_keep_segments = 16   # 80 GB required on pg_xlog


cp /usr/local/pgsql/share/recovery.conf.sample  /data/recovery.cone

vim reconver.conf

standby_mode = on

primary_conninfo = 'host=master port=5433 user=postgres'  #从节点信息


6、生成备库实例

pg_ctl –D $PGDATA -p 5432

传送数据文件到slave

在备库执行

pg_basebackup -D $PGDATA -Fp -Xs -v  -h master -p 5432 -U postgres

7、Slave 配置文件修改


vim postgresql.conf

注意删除 "#"
hot_standby = on   


vim reconver.conf

standby_mode = on

primary_conninfo = 'host=master port=5432 user=postgres'  #主节点信息


8、启动主从数据库

pg_ctl –D $PGDATA

master

[postgres@localhost data]$ ps -ef |grep postgres |grep sender
postgres 12021 10924  0 14:37 ?        00:00:00 postgres: wal sender process postgres 172.16.0.132(33427) streaming 0/3036838

slave
[postgres@localhost data]$ ps -ef |grep postgres |grep recover                   
postgres  5479  5471  0 17:24 ?        00:00:00 postgres: startup process   recovering 00000002000000000000000D


注意：这个时候slave从master同步数据，但是slave 是只读的。

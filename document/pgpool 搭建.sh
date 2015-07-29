
进行pgpool搭建前需要配置好postgresql的流复制，操作步骤参考http://xiajie.blog.51cto.com/6044823/1662222
原理参考：http://dz.sdut.edu.cn/blog/subaochen/?p=430
一、安装
 wget http://www.pgpool.net/download.php?f=pgpool-II-3.4.0.tar.gz
 tar -zxvf pgpool-3.4.0.tar.gz
 cd pgpool-II-3.4.0/
 ./configure --prefix=/usr/local/pgpool --with-pgsql=path --with-pgsql=/usr/local/pgsql
 make
 make install
 chown postgres.postgres /usr/local/pgpool/ -R
 chown postgres.postgres /usr/src/pgpool-II-3 -R
 mkdir /var/run/pgpool
 chown postgres.postgres /var/run/pgpool/
 #切换postgres 用户安装一些函数
 su - postgres
 
 cd /usr/src/pgpool-II-3.4.0/src/sql/
 make
 make install
 cd pgpool-recovery/
 make install
 cd ../pgpool-regclass/
 make install
 
二、配置

 cd /usr/local/pgpool/etc
 cp pcp.conf.sample pcp.conf
 pg_md5 postgres
 e8a48653851e28c69d0506508fb27fc5
 echo "postgres:e8a48653851e28c69d0506508fb27fc5" >> pcp.conf
 echo "postgres:e8a48653851e28c69d0506508fb27fc5" >> pool_passwd
 cp pool_hba.conf.sample pool_hba.conf

 vim pool_hba.conf
 host    all         postgres    db2                   md5
 
 
 listen_addresses = '*'					#允许所有主机监听
 port = 9999							#访问端口
 backend_hostname0 = 'db1'				#DBmaster ip
 backend_port0 = 5432					#DBmaster postgresql 端口
 backend_weight0 = 1					#权重
 backend_data_directory0 = '/opt/data'	#DBmaster 数据库目录
 backend_flag0 = 'ALLOW_TO_FAILOVER'	#允许切换
 
 backend_hostname0 = 'db2'
 backend_port0 = 5432
 backend_weight0 = 1
 backend_data_directory0 = '/opt/data'
 backend_flag0 = 'ALLOW_TO_FAILOVER'
 
 enable_pool_hba = on   #随意，自由定制，使用 pool_hba.conf 对client的验证
 pool_passwd = 'pool_passwd' #md5验证文件

 sr_check_user = 'postgres'  #用来故障切换的用户
 
 failover_command = '/usr/local/pgsql/bin/failover_command.sh %d %H /tmp/trigger_file' 
#故障切换脚本
 
 
 vim /usr/local/pgsql/bin/failover_command.sh
 
#! /bin/sh
# Failover command for streaming replication.
# This script assumes that DB node 0 is primary, and 1 is standby.
# 
# If standby goes down, do nothing. If primary goes down, create a
# trigger file so that standby takes over primary node.
#
# Arguments: $1: failed node id. $2: new master hostname. $3: path to
# trigger file.

failed_node=$1
new_master=$2
trigger_file=$3

# Do nothing if standby goes down.
#if [ $failed_node = 1 ]; then
#       exit 0;
#fi

# Create the trigger file.
/usr/bin/ssh -T $new_master /bin/touch $trigger_file

exit 0;

chmod +x /usr/local/pgsql/bin/failover_command.sh

三、调试

 #启动命令，带有日志输出
 [postgres@db1 etc]$ pgpool -nd >/tmp/pgpool.log 2>&1 &
 postgres@db1 etc]$ netstat -ntlp
 (Not all processes could be identified, non-owned process info
  will not be shown, you would have to be root to see it all.)
 Active Internet connections (only servers)
 Proto Recv-Q Send-Q Local Address               Foreign Address             State       PID/Program name   
 tcp        0      0 0.0.0.0:22                  0.0.0.0:*                   LISTEN      -                   
 tcp        0      0 127.0.0.1:25                0.0.0.0:*                   LISTEN      -                   
 tcp        0      0 0.0.0.0:9898                0.0.0.0:*                   LISTEN      16664/pgpool        
 tcp        0      0 0.0.0.0:9999                0.0.0.0:*                   LISTEN      16664/pgpool        
 tcp        0      0 :::22                       :::*                        LISTEN      -                   
 tcp        0      0 ::1:25                      :::*                        LISTEN      -                   
 tcp        0      0 :::9999                     :::*                        LISTEN      16664/pgpool      
 
 #登录
[postgres@db1 etc]$ psql -U postgres -h db1 -p 9999
 psql (9.2.1)
 Type "help" for help.

 postgres=# show pool_nodes;
 node_id | hostname | port | status | lb_weight |  role   
---------+----------+------+--------+-----------+---------
 0       | db1      | 5432 | 2      | 0.500000  | primary
 1       | db2      | 5432 | 2      | 0.500000  | standby
(2 rows)
 postgres=# create database db0;
 CREATE DATABASE

2：启动
3：死啦

#测试可以登录，可以读写

四、故障切换

#首先停止DBmaster
[postgres@db1 etc]$ pg_ctl -m fast stop

#登录查看
[postgres@db1 etc]$ psql -U postgres -h db1 -p 9999
 postgres=# show pool_nodes;
 node_id | hostname | port | status | lb_weight |  role   
---------+----------+------+--------+-----------+---------
 0       | db1      | 5432 | 3      | 0.500000  | standby
 1       | db2      | 5432 | 2      | 0.500000  | primary
(2 rows)

#此时DBslave显示的日志信息

[postgres@db2 data]$ FATAL:  replication terminated by primary server
LOG:  record with zero length at 0/10000FE0
LOG:  trigger file found: /tmp/trigger_file
LOG:  redo done at 0/10000F80
LOG:  last completed transaction was at log time 2015-06-17 11:05:44.379009+08
LOG:  selected new timeline ID: 2
LOG:  archive recovery complete
LOG:  database system is ready to accept connections
LOG:  autovacuum launcher started


#DBmaster 已经死啦，状态切换为standby；DBslave切换为primary；测试可读写
#日志提示，发现 trigger_file文件，进行切换
#DBslave 切换为 主服务器
#recover.conf自动更改为recover.done
[postgres@db2 data]$ ll /opt/data/recovery.done 

故障切换成功

五、恢复DBmaster

1、同步DBmaster至DBslave
pg_basebackup -D $PGDATA -Fp -Xs -v  -h db1 -p 5432 -U postgres
2、修改配置文件
listen_addresses = '*' 
port = 5432
hot_standby = on
3、修改recover文件
mv recover.done  recover.conf

vim recover.conf
primary_conninfo = 'host=172.16.0.133 port=5432 user=postgres'
4、启动DBslave
5、添加node
pcp_attach_node -d 5 db1 9898 postgres postgres 0
pcp_attach_node -d 5 db1 9898 postgres postgres 1

登录查看

postgres=# show pool_nodes;
node_id | hostname | port | status | lb_weight |  role   
---------+----------+------+--------+-----------+---------
 0       | db1      | 5432 | 2      | 0.500000  | primary
 1       | db2      | 5432 | 2      | 0.500000  | standby
(2 rows)


恢复正常
Game Over ！




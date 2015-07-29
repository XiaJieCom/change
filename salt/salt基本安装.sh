一、安装

rhel（centos）5：
rpm -Uvh http://mirror.pnl.gov/epel/5/i386/epel-release-5-4.noarch.rpm  （不好用请在网上找源）
	
cd /etc/yum.repos.d/
wget http://copr.fedoraproject.org/coprs/saltstack/salt-el5/repo/epel-5/saltstack-salt-el5-epel-5.repo
yum install salt-minion -y

	
rhel（centos）6：rpm -Uvh http://mirrors.sohu.com/fedora-epel/6/x86_64/epel-release-6-8.noarch.rpm  

server端：

yum install salt-master -y

vim /etc/salt/master

file_roots:
 base:
  - /srv/salt/

log_file: /var/log/salt/master
key_logfile: /var/log/salt/key

/etc/init.d/salt-master start

client端：

yum install salt-minion -y

vim /etc/salt/minion 

master:master
user:root
id:client-01
log_file: /var/log/salt/minion
key_logfile: /var/log/salt/key
schedule:
  highstate:
    function: state.highstate
    minutes: 60

/etc/init.d/salt-minion start

二、初步配置

[root@master salt]# ll
total 16
drwxr-xr-x. 2 root root 4096 Jun 28 20:56 dev
drwxr-xr-x. 2 root root 4096 Jun 28 21:25 _modules
drwxr-xr-x. 2 root root 4096 Jun 15 03:08 nginx
-rw-r--r--. 1 root root   27 Jun 28 20:56 top.sls

1、新建top.sls 

[root@master salt]# cat top.sls 
base:
  '*':
  - dev.nginx

[root@master salt]# cat dev/nginx.sls 
nginx:
  pkg:
    - installed
  service:
    - running
    - enable: Ture
    - watch:
      - file: /etc/nginx/nginx.conf
      - file: /etc/nginx/conf.d/default.conf
    - require:
      - pkg: nginx
/etc/nginx/nginx.conf:
  file.managed:
    - source: salt://nginx/nginx.conf
    - mode: 664
    - user: root
    - group: root
/etc/nginx/conf.d/default.conf:
  file.managed:
    - source: salt://nginx/default.conf
    - mode: 664
    - user: root
    - group: root

[root@master salt]# ll nginx/
total 8
-rw-r--r--. 1 root root 605 Jun 15 03:08 default.conf
-rw-r--r--. 1 root root 642 Jun 15 03:08 nginx.conf

http://www.saltstack.cn/projects/cssug-kb/wiki/Salt-016-install-and-manager
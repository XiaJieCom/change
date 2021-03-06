http://blog.csdn.net/zdwzzu2006/article/details/7713596
netstat -n | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'


0、开启web服务


    python -m SimpleHTTPServer 80801

1、检查nagios语法
usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg    
2、添加一个用户，无主目录，无法登录
useradd -M -s /sbin/nologin hi
3、新建samba用户
[root@linux samba]# smbpasswd -a samba  
（-a必须加，为了生成密码文件smbpasswd，该密码是windows登陆Linux的samba用户密码）
4、samba配置文件
/etc/samba/smb.conf
可以修改用户权限
5、perl 已安装模块查看
perldoc -t perllocal |grep Module


7、重新挂载磁盘时，遇到 device is  busy
 umount -l /dev/samba

 -l   代表在设备空闲时自动卸载

8、 检查CPU是否支持虚拟化
	在终端执行cat /proc/cpuinfo命令，找到flags部分，如果其中输出有VMX或SVM，即表明支持虚拟化技术。
	cat/proc/cpuinfo | grep vmx       ##(for Intel CPU)
	or 
	cat /proc/cpuinfo | grep svm       ##（for AMD CPU）

9、僵死进程查看，处理

ps -ef | grep defunct
ps -ef | grep defunct | grep -v grep | wc -l
ps -e -o ppid,stat | grep Z | cut -d” ” -f2 | xargs kill -9

10、state 状态防火墙
	--state NEW        建立新的连接
	--state ESTABLISHED 已建立连接
	--state RELATED        相关的
	--state INVALID        无效的

对于web服务器来说 iptables 的状态检测，established 代表已经建立的连接，也就是说只允许已经建立的连接再次访问。所以如果这样的话，新的客户端是被禁止访问的

正常

ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0           state RELATED,ESTABLISHED 
ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           state NEW tcp dpt:80 
ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           state NEW tcp dpt:82 
ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           state NEW tcp dpt:83

错误

ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0           state RELATED,ESTABLISHED 
ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           tcp dpt:1080 state ESTABLISHED 
ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           tcp dpt:80 state ESTABLISHED 

11、删除文件

find . -name XXX -exec mv {} /tmp/ts \;

12、tar排除文件

tar -zcvf XXX.tar.gz --exclude=XXXX/log* aaa/
tar -zcvf ermupdatenew.tar.gz --exclude=ermupdatenew/log* ermupdatenew/

13、查找超过1G的文件

find / -size +1000000000c


14、解压tar.xz 文件


	yum install xz -y
	
    $xz -d ***.tar.xz

    $tar -xvf  ***.tar
	
15、主机探索或者 ping 扫描：

    nmap -sP 192.168.1.0/24
16、reboot  和 shutdown -r now 的区别
	
	shutdown命令可以安全地关闭或重启Linux系统，它在系统关闭之前给系统上的所有登录用户提示一条警告信息。该命令还允许用户指定一个时间参数，可以是一个精确的时间，也可以是从现在开始的一个时间段。
	halt是最简单的关机命令，其实际上是调用shutdown -h命令。halt执行时，杀死应用进程，文件系统写操作完成后就会停止内核。
	reboot命令重启动系统时是删除所有的进程，而不是平稳地终止它们。因此，使用reboot命令可以快速地关闭系统，但如果还有其它用户在该系统上工作时，就会引起数据的丢失。所以使用reboot命令的场合主要是在单用户模式。
	init是所有进程的祖先，其进程号始终为1。init用于切换系统的运行级别，切换的工作是立即完成的。init 0命令用于立即将系统运行级别切换为0，即关机；init 6命令用于将系统运行级别切换为6，即重新启动
17、测试磁盘写入速度
    dd if=/dev/zero of=/tmp/output.img bs=8k count=256k conv=fdatasync; rm -rf /tmp/output.img
	
    dd – 转换和复制文件
    if=/dev/zero – 指定输入文件，默认为stdin（标准输入）
    of=/tmp/output.img – 指定输出文件，默认为stdout（标准输出）
    bs – 一次读和写的块大小，最大可以以MB为单位
    count – 复制次数
    conv – 使用逗号分隔的策略来转换文件（LCTT 译注：比如将大写字母转换成小写，echo AA | dd conv=lcase）
    rm – 删除文件和目录
    -rf – （-r） 递归地删除目录和其中的内容，（-f）强行删除而不输出确认信息
18、vim 
	跳转到页首  gg
	跳转到页尾	G
	统计某单词出现的次数 :%s/xxx/&/g
	删除到页尾	:1,$d
	撤销修改: U
	恢复修改: ctrl+r
19、时间同步
	ntpdate asia.pool.ntp.org
20、查找并移动
	把当前目录下面的file（不包括目录)，移动到/opt/shell
	find  .  -type f  -exec mv {}   /opt/shell   \;
21、检查udp端口
	nc -vuz 127.0.0.1 123
22、xm基本命令

　　xm list：所有已知的虚拟机列表
　　xm create：启动一个非托管的虚拟机
　　xm help：所有可用的xm命令概述
　　xm top：提供所有虚拟机的状态概貌
　　xm console：打开控制台管理虚拟机
　　xm new：添加虚拟机到Xenbase托管环境
　　xm start：从Xenbase托管环境启动虚拟机
　　xm destroy：像关掉电源那样关闭虚拟机
　　xm shutdown：正确地关掉虚拟机
　　xm reboot：重新启动虚拟机
　　xm pause：暂停虚拟机的活动而不释放使用的内存资源
　　xm unpause：激活使用xm pause命令暂停的虚拟机
　　xm save：保存虚拟机状态到一个文件
　　xm restore：重新启动已经保存在文件里的虚拟机

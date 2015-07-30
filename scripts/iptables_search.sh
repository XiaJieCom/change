iptables -F 清空所有规则链
iptables -X 删除特定手工设置的链
iptables -Z 清空计数器
iptables -P INPUT DROP //默认INPUT规则 丢弃
iptables -P OUTPUT DROP //默认OUTPUT规则 丢弃
iptables -P FORWARD DROP //默认FORWARD规则 丢弃
iptables -A INPUT -d 192.168.10.250 -p tcp -m tcp --dport 22 -j ACCEPT //开SSH服务进站端口
iptables -A INPUT -d 192.168.10.250 -p tcp -m tcp --dport 80 -j ACCEPT //开WEB服务进站端口
iptables -A INPUT -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT //允许本地环回数据
iptables -A INPUT -p udp -m udp --sport 53 -j ACCEPT  //来自远程DNS服务器53端口的数据包进站通过
iptables -A INPUT -p udp -m udp --dport 53 -j ACCEPT  //进入本地服务器53端口的数据包进站通过
iptables -A INPUT -d 192.168.10.250 -p icmp -j ACCEPT //ICPM数据包可进入本地服务器
         
iptables -A OUTPUT -s 192.168.10.250 -p tcp -m tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT //对SSH的服务进入的数据包开启出站端口
iptables -A OUTPUT -s 192.168.10.250 -p tcp -m tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT //对WEB的服务进入的数据包开启出站端口
iptables -A OUTPUT -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT //允许本地环回数据
iptables -A OUTPUT -p udp -m udp --sport 53 -j ACCEPT  //从本地53端口出站的数据包出站通过
iptables -A OUTPUT -p udp -m udp --dport 53 -j ACCEPT  //去往远程DNS服务器53端口的数据包出站通过
iptables -A OUTPUT -s 192.168.10.250 -p icmp -j ACCEPT //对对方ICMP数据包回应(ping命令回应数据包)
service iptables save //保存配置信息
service iptables start //开启防火墙服务

​iptables -P INPUT DROP 
iptables -P OUTPUT DROP 
iptables -P FORWARD DROP 
iptables -A INPUT -s 203.187.177.128/27 -p tcp --dport 8567  -m state --state ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp -m tcp --dport 80  -m state --state ESTABLISHED -j ACCEPT 
iptables -A INPUT -p udp -m udp --sport 53 -j ACCEPT  
iptables -A INPUT -p udp -m udp --dport 53 -j ACCEPT
iptables -A INPUT -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT 
iptables -A INPUT -p icmp -j ACCEPT    
iptables -A OUTPUT -p udp -m udp --sport 53 -j ACCEPT  
iptables -A INPUT -i lo -p all -j ACCEPT
iptables -A OUTPUT -s 203.187.177.128/27 -p tcp --sport 8567  -m state --state ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp -m tcp --sport 80  -m state --state ESTABLISHED -j ACCEPT 
iptables -A OUTPUT -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT 
iptables -A OUTPUT -p icmp -j ACCEPT
iptables -A OUTPUT -p udp -m udp --dport 53 -j ACCEPT  
iptables -A OUTPUT -o lo -p all -j ACCEPT





service iptables save 

chkconfig --level 2345 yum-updatesd off
chkconfig --level 2345 sendmail off


iptables -A INPUT -s 203.187.177.128/27  -j ACCEPT
iptables -A INPUT -s 101.251.195.32/27 -j ACCEPT

iptables -A INPUT -s 119.254.12.49/28  -j ACCEPT





















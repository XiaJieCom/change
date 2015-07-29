系统搭建手册
一套系统包含的内容有b2b网站，webservice(cloudwebservice /webpassportwebservice/addresswebservice/tokenwebservice/momsendwebservice),activemq服务，erm，报表服务，附件服务等，具体的配置如下：

一．	B2B网站的相关配置
1.databasewrite.config
配置SQL连接语句数据库为B2B的数据库
需要配置的键值：userid、password、database、datasource、port
2.Web.config
配置appSettings下ticketTimeout节点 value值（配置登陆超时时间）
配置appSettings下PassportWebServiceUrl节点value值为passport的WebService地址
配置appSettings下ErmWebServiceUrl节点value值为erm提供业务交互的WebService地址配置appSettings下AddressServiceUrl节点value值为登陆到erm后台的寻址簿的地址
配置appSettings下PsSecretInPF节点value值为b2bwebservice地址
配置appSettings下CookieDomain节点value值为访问b2b的域名
配置appSettings下B2BUploadServer节点value值为b2b加载图片用的服务地址
配置appSettings下ErmPicServer节点value值为图片服务器的地址
配置appSettings下MOMServer节点value值为接收消息的服务地址
3. SmtpService.xml（邮件服务器的相关配置）
ServerName:邮件服务器名称
Port：邮件服务器端口号
UserName：用户名
Password：密码
4. Setting/registerconfig.config   Setting/appversion.config
这个配置文件主要用来配置站点的内容
注意: Setting/registerconfig.config 的id的唯一性

二．	Webservice的相关配置
1.CloudserviceWebservice(辅助b2b网站显示数据的服务)
1) databasewrite.config
配置SQL连接语句数据库为B2B的数据库
需要配置的键值：userid、password、database、datasource、port
其余默认即可
2) Web.config
配置appSettings下
AddressServiceUrl节点value值为地址簿WebService地址
ErmWebServiceUrl节点value值为ERM 的WebService地址
2.Webpassport Webservice(集成登陆)
1) sqlmapwrite.config
配置SQL连接语句数据库为B2B的数据库
需要配置的键值：server、user id、password、datasource、port
2)Web.config
配置appSettings下
1）TokenWebServiceUrl节点value值为TokenService的WebService地址
2）ERMLoginPassportWebUrl节点value值为ERM的WebService地址
3）AddressServiceUrl节点下vaue值为地址簿的地址
3.AddressWebservice(账号管理服务)
1) sqlmapwrite.config
配置SQL连接语句数据库为MOM的数据库
需要配置的键值：server、user id、password、datasource、port
其余默认即可
2) userparams.conf
<ap id="0">别墅
<maxCustomers>节点value值为免费版允许加客户的个数
<ap id="1">免费版
<maxCustomers>节点value值为免费版允许加客户的个数
<ap id="2">收费版
<maxCustomers>节点value值为收费版允许加客户的个数
<ap id="3">VIP版
<maxCustomers>节点value值为收费版允许加客户的个数
4.MomSendWebservice(erm发数据到b2b的服务)
1) Web.config
配置appSettings下
BROKER节点value值为MQ后台服务启动的端口的地址
MOMConnStr节点value值为MOM服务数据库连接地址
CLIENTID节点value值为MOM客户端标识（能够区分开就可以）
5.ErmWebservice(erm之间交互处理数据的服务)
1)Proxy.config
配置域名所对应的的后台端口
6.TokenWebservice(控制系统在线人数的服务)
三．	MQ的相关配置(处理消息队列)
1.	要在/usr/share/下建立一个.mono/keypairs/的目录，目录的属主为apache用户，权限为775
2.	conf/activemq.xml 节点openwire要配置MQ服务本身需要的tcp端口
   <plugins>
            <simpleAuthenticationPlugin>
                <users>
                   <authenticationUser username="universal3" password="universal3" groups="users,admins"/>
                </users>
            </simpleAuthenticationPlugin>
        </plugins>这里的username和password是ermapp请求MQ服务的密钥
3.	conf/jetty.xml  设置一个mq  http的端口 
4.	conf/jmx.password 设置访问mq客户端的用户和密码
5.	conf/jmx.access 设置mq客户端的用户的权限
四．	Erm的相关配置
1.	ERMAPP(业务后台)
1）bin\mono-service.exe.config
配置appSettings下
a．SystemID节点value值为调用MOM的标识(一般不用修改)
b．AddressServiceUrl节点为地址簿WEBService地址
c．PackageTypeServiceUrl节点为地址簿WEBService地址
d. PassortServiceUrl节点为passportWebservice的地址
f. B2BServiceUrl节点为ermwebservice的地址
g. FileTranUrl 节点为读取附件服务文件的地址
h．RAQReportURL 节点为润乾V5报表服务的地址
I．MOMServer 节点momsendwebservice的地址
2） bin/log4net.config
配置ConnectionString节点，这个文件主要是用来输出错误日志
3）Configuration/Agent.config
配置broker后台地址
4）Configuration/DataBase.config
配置各个域的数据库连接字符串
5）Configuration/Domain.config
配置启动域的相关参数ParentDomain为父域，
<DomainItem Name="Public" ParentDomain ="" State="1" DeployType ="0" LogOnOff="0" Activemq="activemq:failover:(tcp://demo5.biswit.com:1791)" AppVersion="app_20130621" Username="universal3" PassWord="universal3"/>
<DomainItem Name="universal" ParentDomain ="Public" State="1" DeployType ="0" LogOnOff="0" Activemq="activemq:failover:(tcp://demo5.biswit.com:1791)" AppVersion="app_20130621"/>
Activemq的值为mq服务启动的tcp端口，AppVersion记录升级的版本号，Username和passowrd请求mq服务的密钥。
6）Configuration/Proxy.config
配置broker后台地址
7）Configuration/Remoting.config
配置broker后台端口
8) Configuration/MobileVersion.xml
配置手机客户端的地址，version的值不能随意换
9）Domain/域/Configuration/RecordID.config
配置起始ID（注意多个域时要配置多个）
2. DeployApp(bitmap服务端，新部署域后要提供给客户端bitmap的服务端的端口、域名、IP)
1）DeployApp/AppConfig.xml
appserverpath节点为ermapp所在路径
webserverpath节点为ermweb所在路径
svnurl节点为erm托管的svn地址
svnscript 节点为提交bitmap发布的模型的脚本
2）DeployApp/Remoting.config
主要配置port端口(配置前注意看一下所配置的端口是否被占用)
3）Web
如果有新增域名的话要配置一个重定向到ermweb的软连接(主要是bitmap发布模型到前台)
3. Ermweb(业务前台展示)
1）Configuration/Proxy.config 
配置ermapp后台的端口
Configuration/ReportUrlConfig.xml 使用V4报表的访问地址
2）Web.Config 配置appSettings下
Domain 的值为后台对应的域名
UploadServerUrl 的值为附件服务地址
ReportServerUrl 的值为普通报表的地址
B2BLogoServerUrl的值为图片服务器的地址
ticketTimeout的值为系统超时时间
B2BUrl节点value值为B2B网站地址
PassportWebServiceUrl节点value值为passport地址
AddressServiceUrl节点value值为地址簿的webservice地址
CookieDomain 的值为登陆系统的缓存域名

注意：以上服务需要记录程序产生的日志和某些文件的读写权限，所以要给对应服务下的文件赋予相应权限！
五．数据库
 注意:一个项目对应一套数据库，访问数据库的用户、密码以及数据名称都要按照当前环境的命名规则来
六．项目还需要部署一些辅助工具的服务
1.润乾报表服务
见文档《润乾报表的配置.doc》
2.普通报表服务
   需要修改Proxy.xml 这个跟ermapp后台配置文件Proxy.xml一样，然后发布到iis
3.附件服务
   只需要把程序部署到iis上
4.图片上传服务
只需要把程序部署到iis上

1、复制单个文件到client

salt '*' cp.get_file salt://vimrc /etc/vimrc

参考格式
salt '*' cp.get_file "salt://{{grains.os}}/vimrc" /etc/vimrc template=jinja

2、传输时开启压缩模式，级别 1-9
对于大文件，cp.get_file支持gzip压缩，在参数中指定gzip的压缩级别，如下:
 salt '*' cp.get_file salt://vimrc /etc/vimrc gzip=5

3、如果目标机器没有该目录，使用makedirs=True 自动创建
 salt '*' cp.get_file salt://vimrc /etc/vim/vimrc makedirs=True

4、传输整个目录到目标机器 

cp.get_dir可以从master下载整个目录，语法如下：
 salt '*' cp.get_dir salt://etc/apache2 /etc

5、传输目录时开启gzip压缩

cp.get_dir也支持模板和压缩：
 salt '*' cp.get_dir salt://etc/{{pillar.webserver}} /etc gzip=5 template=jinja
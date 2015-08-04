#该脚本主要功能是使用python生成pdf文件。依赖python-reportlab模块。
	disk_report()return该文件的内容
	create_pdf()根据return输出到pdf文件
#安装方式	
	yum install python-reportlab 

示例一、生成一段文字
#!/usr/bin/python
from reportlab.pdfgen import canvas
def hello():
    c = canvas.Canvas("helloworld.pdf")
    c.drawString(100,100,"Hello,World")
    c.showPage()
    c.save()
hello()


示例二、生成单个文件的pdf

#!/usr/bin/python

import datetime
import subprocess
import codecs
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4, landscape
import reportlab.pdfbase.ttfonts  
reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('song', '/usr/share/fonts/cn/msjh.ttf'))  
import reportlab.lib.fonts  



def disk1_report():
 p1 = subprocess.Popen("cat cmd1.log ",shell=True,stdout=subprocess.PIPE)
 return p1.stdout.readlines()
def create_pdf(input,output="disk1.pdf"):
 now = datetime.datetime.today()
 date = now.strftime("%h %d %Y %H:%M:%S")
 c = canvas.Canvas(output,pagesize=A4)
 c.setFont('song',10)
 textobject = c.beginText()
 textobject.setTextOrigin(1*inch,11*inch)
 textobject.textLines('''Disk Capacity Report: %s ''' % date )
 for line in input:
  textobject.textLine(line.strip())
 c.drawText(textobject)
 c.showPage()
 c.save()
report = disk1_report()
create_pdf(report)

示例三、循环生成指定目录下的多个文件（）
#需要安装字体 yum install wqy-* -y
#!/usr/bin/python

import os
import os.path
import datetime
import subprocess
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

logdir = "/var/www/device/check_log"

for root,dirs,filenames in os.walk(logdir):
  for filename in filenames:
    v = root+os.sep+filename
    os.environ['file'] = str(v)
    def disk_report():
      p = subprocess.Popen("cat $file ",shell=True,stdout=subprocess.PIPE)
      return p.stdout.readlines()
    def create_pdf(input,output="/var/www/device/check_pdf/"+filename+".pdf"):
     now = datetime.datetime.today()
     date = now.strftime("%h %d %Y %H:%M:%S")
     c = canvas.Canvas(output,pagesize=A4)
     textobject = c.beginText()
     textobject.setTextOrigin(1*inch,11*inch)
     textobject.textLines('''Disk Capacity Report: %s ''' % date )
     for line in input:
      textobject.textLine(line.strip())
     c.drawText(textobject)
     c.showPage()
     c.save()
    report = disk_report()
    create_pdf(report)
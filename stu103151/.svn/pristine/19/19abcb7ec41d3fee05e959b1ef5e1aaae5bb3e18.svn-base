from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(u'姓名',max_length=32)
    def __str__(self):
        return '%s' %self.name
    class Meta:
        verbose_name = '讲师信息'
        verbose_name_plural = '讲师信息'
class School(models.Model):
    name = models.CharField(u'校区名称',max_length=64,unique=True)
    addr = models.CharField(u'地址',max_length=128)
    staffs = models.ManyToManyField('UserProfile',blank=True)
    class Meta:
        verbose_name = '校区信息'
        verbose_name_plural = '校区信息'
    def __str__(self):
        return '%s' %self.name

class Course(models.Model):
    name = models.CharField(u'课程名称',max_length=128,unique=True)
    price = models.IntegerField(u'面授价格')
    online_price = models.IntegerField(u'网络班价格')
    brief = models.TextField(u'课程简介')
    def __str__(self):
        return '%s' %self.name
    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = '课程信息'

class_type_choices = (('online',u'网络班'),
                      ('offline_weekend',u'面授班（周末）'),
                      ('offline_fulltime',u'面授班（脱产）'),
                      )
class ClassList(models.Model):
    course = models.ForeignKey('Course')
    course_type = models.CharField(u'课程类型',choices=class_type_choices,max_length=32)
    semster = models.IntegerField(u'学期')
    star_date = models.DateField(u'开班日期')
    gratute_date = models.DateField(u'结业日期',blank=True,null=True)
    teachers = models.ManyToManyField(UserProfile,verbose_name=u'讲师')
    def __str__(self):
        return '%s' %self.course
    class Meta:
        verbose_name = u'班级列表'
        verbose_name_plural = u'班级列表'
        unique_together = ('course','course_type','semster')
class Customer(models.Model):
    qq = models.CharField(u'QQ',max_length=32,unique=True)
    name = models.CharField(u'姓名',max_length=32,blank=True,null=True)
    phone = models.BigIntegerField(u'手机号',blank=True,null=True)
    stu_id = models.CharField(u'学号',blank=True,null=True,max_length=64)
    source_type = (('QQ',u'QQ群'),
                   ('referral',u'内部转介绍'),
                   ('51CTO',u'51CTO'),
                   ('agent',u'招生代理'),
                   ('others',u'其他'),
                   )
    source = models.CharField(u'客户来源',max_length=64,choices=source_type,default='QQ')
    referral_from = models.ForeignKey('self',verbose_name=u'转介绍自学员',help_text=u'若此客户是转介绍自内部学员,请在此处选择内部学员姓名',blank=True,null=True,related_name='internal_referral')
    course = models.ForeignKey(Course,verbose_name=u'咨询课程')
    class_type = models.TextField(u'客户咨询内容详情',help_text=u'客户咨询的大概清空,客户个人信息备注等...')
    status_choices = (('signed',u'已报名'),
                      ('unregistered',u'未报名'),
                      ('graduated',u'已毕业'),
                      )
    status = models.CharField(u'状态',choices=status_choices,max_length=64,default=u'unregistered',help_text='选择客户此时的状态')
    consulant = models.ForeignKey(UserProfile,verbose_name=u'课程顾问')
    date = models.DateField(u'咨询日期',auto_now_add=True)
    class_list = models.ManyToManyField('ClassList',verbose_name=u'已报班级',blank=True)

    def __str__(self):
        return '%s,%s' %(self.qq,self.name)
    class Meta:
        verbose_name = '客户信息'
        verbose_name_plural = '客户信息'
class ConultRecord(models.Model):
    customer = models.ForeignKey(Customer,verbose_name=u'所咨询客户')
    note = models.TextField(u'跟进内容...')
    status_choices = ((1,u'近期无报名计划'),
                      (2,u'1~2个月内报名'),
                      (3,u'1个月内报名'),
                      (4,u'已报名'),
                      )
    status = models.IntegerField(u'状态',choices=status_choices,help_text=u'选择客户此时的状态')
    consulant = models.ForeignKey(UserProfile,verbose_name=u'跟踪人')
    date = models.DateField(u'跟进日期',auto_now_add=True)
    def __str__(self):
        return '%s,%s' %(self.customer,self.status)
    class Meta:
        verbose_name = u'咨询记录'
        verbose_name_plural = u'咨询记录'

class CourseRecord(models.Model):
    course = models.ForeignKey(ClassList,verbose_name=u'班级（课程）')
    day_num = models.IntegerField(u'节次',help_text=u'此处填写第几节课或第几天课程...必须为数字')
    date = models.DateField(auto_now_add=True,verbose_name='上课日期')
    teacher = models.ForeignKey(UserProfile,verbose_name=u'讲师')
    def __str__(self):
        return '%s第%s天' %(self.course,self.day_num)
    class Meta:
        verbose_name = u'上课记录'
        verbose_name_plural = u'上课记录'
        unique_together = ('course','day_num')



class StudyRecord(models.Model):
    course_record = models.ForeignKey(CourseRecord,verbose_name=u'第几天课程')
    student = models.ForeignKey(Customer,verbose_name=u'学员')
    record_choices = (('checked',u'已签到'),
                      ('late',u'迟到'),
                      ('noshow',u'缺勤'),
                      ('leave_early',u'早退'),
                      )



    record = models.CharField(u'上课记录',choices=record_choices,default='checked',max_length=64)
    score_choices = ((100,'A+'),
                     (90,'A'),
                     (85,'B+'),
                     (80,'B'),
                     (70,'B-'),
                     (60,'C+'),
                     (0,'D'),
                     (-1,'N/A'),
                     (-100,'COPY'),
                     (-1000,'FAIL'),
                     )
    score = models.IntegerField(u'本节课成绩',choices=score_choices,default=-1)
    date = models.DateField(auto_now_add=True)
    note = models.CharField(u'备注',max_length=255,blank=True,null=True)

    def __str__(self):
        return u"%s,学员:%s,纪录:%s, 成绩:%s" %(self.course_record,self.student.name,self.record,self.get_score_display())

    class Meta:
        verbose_name = u'学习纪录'
        verbose_name_plural = u"学习纪录"
        unique_together = ('course_record','student')

    def colored_status(self):
        if self.record == 'checked':
            format_td = format_html('<span style="padding:2px;background-color:green;color:white">已签到</span>')
        elif self.record == 'late':
            format_td = format_html('<span style="padding:2px;background-color:yellow;color:white">迟到</span>')
        elif self.record == 'noshow':
            format_td = format_html('<span style="padding:2px;background-color:red;color:white">缺勤</span>')
        else:
            format_td = format_html('<span style="padding:2px;background-color:black;color:white">早退</span>')
        return  format_td
    colored_status.short_description = 'status'

















#_*_coding:utf-8_*_
from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError

from django.db import models
from django.contrib.auth.models import User
course_type_choices = (('online',u'网络班'),
                        ('offline_weekend',u'面授班(周末)',),
                        ('offline_fulltime',u'面授班(脱产)',),
                        )
class School(models.Model):
    name = models.CharField(max_length=128,unique=True)
    city = models.CharField(max_length=64)
    addr = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=64)
    school = models.ForeignKey('School')

    def __str__(self):
        return self.name
    class Meta:
        permissions =(('view_customer_list', u"可以查看客户列表"),
                      ('view_customer_info',u"可以查看客户详情"),
                      ('edit_own_customer_info',u"可以修改客户信息"),
                      ('view_user_list', u"可以查看用户列表"),
                      ('view_user_info',u"可以查看用户详情"),
                      ('edit_own_user_info',u"可以修改用户信息"),
                      ('view_course_list', u"可以查看课程列表"),
                      ('view_course_info',u"可以查看课程详情"),
                      ('edit_own_course_info',u"可以修改课程信息"),
                      ('view_class_list', u"可以查看班级列表"),
                      ('view_class_info',u"可以查看班级详情"),
                      ('edit_own_class_info',u"可以修改班级信息"),
                      ('view_school_list', u"可以查看校区列表"),
                      ('view_school_info',u"可以查看校区详情"),
                      ('edit_own_school_info',u"可以修改校区信息"),

                      )
class Role(models.Model):
    name = models.CharField(max_length=32,unique=True)
    member = models.ManyToManyField('UserProfile')
    pass
class Customer(models.Model):
    qq = models.CharField(max_length=64,unique=True)
    name = models.CharField(max_length=32,blank=True,null=True)
    phone = models.BigIntegerField(blank=True,null=True)
    course = models.ForeignKey('Course')
    course_type = models.CharField(max_length=64,choices=course_type_choices,default='offline_weekend')
    consult_memo = models.TextField()
    source_type_choices = (('qq',u"qq群"),
                   ('referral',u"内部转介绍"),
                   ('51cto',u"51cto"),
                   ('agent',u"招生代理"),
                   ('others',u"其它"),
                   )
    source_type = models.CharField(max_length=64,choices=source_type_choices)
    referral_from = models.ForeignKey('self',blank=True,null=True,related_name="referraled_who")
    status_choices = (('signed',u"已报名"),
                      ('unregistered',u"未报名"),
                      ('graduated',u"已毕业"),
                      ('drop-off',u"退学"),
                      )
    status = models.CharField(choices=status_choices,max_length=64)
    consultant = models.ForeignKey('UserProfile',verbose_name=u"课程顾问")
    class_list = models.ManyToManyField("ClassList",blank=True)
    date = models.DateField(u"咨询日期",auto_now_add=True)

    def __str__(self):
        return "%s(%s)"%(self.qq,self.name)
class CustomerTrackRecord(models.Model):
    customer = models.ForeignKey(Customer)
    track_record = models.TextField(u"跟踪纪录")
    track_date = models.DateField(auto_now_add=True)
    follower = models.ForeignKey(UserProfile)
    status_choices = ((1,u"近期无报名计划"),
                      (2,u"2个月内报名"),
                      (3,u"1个月内报名"),
                      (4,u"2周内报名"),
                      (5,u"1周内报名"),
                      (6,u"2天内报名"),
                      (7,u"已报名"),
                      )
    status = models.IntegerField(u"状态",choices=status_choices,help_text=u"选择客户此时的状态")
    def __str__(self):
        return self.customer

class Course(models.Model):
    name = models.CharField(max_length=64,unique=True)
    online_price = models.IntegerField()
    offline_price = models.IntegerField()
    introduction = models.TextField()

    def __str__(self):
        return  self.name
class ClassList(models.Model):
    course = models.ForeignKey(Course,verbose_name=u"课程")
    semester = models.IntegerField(verbose_name=u"学期")
    course_type = models.CharField(max_length=64,choices=course_type_choices,default='offline_weekend')
    teachers = models.ManyToManyField(UserProfile)
    start_date = models.DateField()
    graduate_date = models.DateField()

    def __str__(self):
        return "%s(%s)(%s)" %(self.course.name,self.course_type,self.semester)

    class Meta:
        unique_together = ('course','semester','course_type')

class CourseRecord(models.Model):
    class_obj = models.ForeignKey(ClassList)
    day_num = models.IntegerField(u"第几节课")
    course_date = models.DateField(auto_now_add=True,verbose_name=u"上课时间")
    teacher = models.ForeignKey(UserProfile)
    #students = models.ManyToManyField(Customer)
    def __str__(self):
        return "%s,%s"%(self.class_obj,self.day_num)
    class Meta:
        unique_together = ('class_obj','day_num')

class StudyRecord(models.Model):
    course_record = models.ForeignKey(CourseRecord)
    student = models.ForeignKey(Customer)
    record_choices = (('checked', u"已签到"),
                      ('late',u"迟到"),
                      ('noshow',u"缺勤"),
                      ('leave_early',u"早退"),
                      )
    record = models.CharField(u"状态", choices=record_choices,max_length=64)
    score_choices = ((100, 'A+'),
                     (90,'A'),
                     (85,'B+'),
                     (80,'B'),
                     (70,'B-'),
                     (60,'C+'),
                     (50,'C'),
                     (40,'C-'),
                     (0,'D'),
                     (-1,'N/A'),
                     (-100,'COPY'),
                     (-1000,'FAIL'),
                     )
    score = models.IntegerField(u"本节成绩",choices=score_choices,default=-1)
    date = models.DateTimeField(auto_now_add=True)
    note = models.CharField(u"备注",max_length=255,blank=True,null=True)

    def __str__(self):
        return "%s,%s,%s"%(self.course_record,self.student,self.record)
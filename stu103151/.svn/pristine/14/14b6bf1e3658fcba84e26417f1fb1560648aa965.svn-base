from django.contrib import admin
from crm import models
# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name','addr')
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','price','online_price','brief')
class ClassListAdmin(admin.ModelAdmin):
    list_display = ('course','course_type','semster','star_date','gratute_date')
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('qq','name','phone','stu_id','source','class_type','status','date')
class ConultRecordAdmin(admin.ModelAdmin):
    list_display = ('customer','note','status','consulant','date')
class CourseRecordAdmin(admin.ModelAdmin):
    list_display = ('course','day_num','date')
def make_late(modelAdmin,request,queryset):
    queryset.update(record = 'late')
    make_late.short_description = 'Set to late'
def make_noshow(modelAdmin,request,queryset):
    queryset.update(record = 'noshow')
    make_late.short_description = 'Set to noshow'
def make_leave_early(modelAdmin,request,queryset):
    queryset.update(record = 'leave_early')
    make_late.short_description = 'Set to leave_early'
class StudyRecordAdmin(admin.ModelAdmin):
    list_display = ('course_record','record','score','date','note','colored_status')
    actions = [make_late,make_noshow,make_leave_early]

admin.site.register(models.UserProfile)
admin.site.register(models.School,SchoolAdmin)
admin.site.register(models.Course,CourseAdmin)
admin.site.register(models.ClassList,ClassListAdmin)
admin.site.register(models.Customer,CustomerAdmin)
admin.site.register(models.ConultRecord,ConultRecordAdmin)
admin.site.register(models.CourseRecord,CourseRecordAdmin)
admin.site.register(models.StudyRecord,StudyRecordAdmin)

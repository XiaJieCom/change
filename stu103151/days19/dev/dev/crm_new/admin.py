from django.contrib import admin
from crm_new import models

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.School,)
admin.site.register(models.Course,)
admin.site.register(models.ClassList,)
admin.site.register(models.Customer,)
# admin.site.register(models.ConultRecord,ConultRecordAdmin)
admin.site.register(models.CourseRecord,)
admin.site.register(models.StudyRecord,)
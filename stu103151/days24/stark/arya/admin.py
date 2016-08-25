from django.contrib import admin

# Register your models here.
from arya import models

admin.site.register(models.Host)
admin.site.register(models.HostGroup)
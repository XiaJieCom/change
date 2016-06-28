from django.contrib import admin
from blog import models

#Register your models here.
class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline','pub_date','mod_date','n_comments','n_pingbacks')

admin.site.register(models.Author)
admin.site.register(models.Entry,EntryAdmin)
admin.site.register(models.Blog)

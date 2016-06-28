from django.contrib import admin

# Register your models here.

from store import models

def make_forbidden(modelAdmin,request,queryset):
    print('-->',request,queryset)
    queryset.update(status = 'forbidden')
    make_forbidden.short_description = 'Set to forbidden'




class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','publisher','pulication_date','colored_status')
    search_fields = ('name','publisher__name')
    list_filter = ('publisher','pulication_date')
    list_editable = ('name','pulication_date')
    list_per_page = 10
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)
    actions = [make_forbidden,]

admin.site.register(models.Author)
admin.site.register(models.Book,BookAdmin)
admin.site.register(models.Publisher)
admin.site.register(models.UserInfo)

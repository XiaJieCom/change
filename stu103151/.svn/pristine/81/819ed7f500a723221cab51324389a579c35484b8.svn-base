from django.db import models
from django.utils.html import format_html

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    def __str__(self):
        return '%s' %self.username

class Publisher(models.Model):
    name = models.CharField(max_length=32,unique=True)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=32)
    state_province = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    website = models.CharField(max_length=128)
    def __str__(self):
        return '%s' %self.name


class Author(models.Model):
    first_name = models.CharField(max_length=32,unique=True)
    last_name = models.CharField(max_length=32,unique=True)
    email = models.EmailField
    def __str__(self):
        return '%s %s' %(self.first_name,self.last_name)
class Book(models.Model):
    name = models.CharField(max_length=64,unique=True)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    pulication_date = models.DateField()
    status_choices = (('published',u'已出版'),
                      ('producing',u'待出版'),
                      ('forbidden',u'销毁'),
                      )
    status = models.CharField(choices=status_choices,max_length=32,default='producing')
    def __str__(self):
        return '%s' %self.name

    def colored_status(self):
        if self.status == "published":
            format_td =format_html('<span style="padding:2px;background-color:yellowgreen;color:white">已出版</span>')
        elif self.status == "producing":
            format_td =format_html('<span style="padding:2px;background-color:pink;color:white">待出版</span>')
        elif self.status == "forbidden":
            format_td =format_html('<span style="padding:2px;background-color:orange;color:white">禁书</span>')

        return  format_td
    colored_status.short_description = 'status'
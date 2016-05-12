from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=32)
    state_province = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    websit = models.CharField(max_length=128)
    def __str__(self):
        return '<%s>' %self.name


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField
    def __str__(self):
        return '<%s %s>' %(self.first_name,self.last_name)
class Book(models.Model):
    name = models.CharField(max_length=64)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    pulication_date = models.DateField()
    def __str__(self):
        return '<%s>' %self.name
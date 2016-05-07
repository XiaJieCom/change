from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)



class ECSInfo(models.Model):
    '''
    创建服务器列表
    '''
    host = models.CharField(max_length=32)
    ip = models.CharField(max_length=32)
    port = models.CharField(max_length=32)
    status = models.BooleanField(max_length=1)
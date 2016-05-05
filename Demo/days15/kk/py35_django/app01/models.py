from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()
# obj = UserInfo()
# li = [obj1,obj2,obj3]
# for i in li:
#     print(i.username)
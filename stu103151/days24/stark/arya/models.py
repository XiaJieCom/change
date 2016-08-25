from django.db import models

# Create your models here.
class Host(models.Model):
    '''
    主机表,主机名/key/状态/系统类型
    '''
    hostname = models.CharField(max_length=128,unique=True)
    key = models.TextField()
    status_choices = ((0,'Waiting Approval'),
                      (1,'Accepted'),
                      (2,'Rejected'))
    status = models.SmallIntegerField(choices=status_choices,default=0)
    os_type_choices = (('redhat','RedHat\CentOS'),
                       ('ubuntu','Ubuntu'),
                       ('suse','SUSE'),
                       ('windows','Windows'))
    os_type = models.CharField(choices=os_type_choices,max_length=64,default='redhat')


    def __str__(self):
        return self.hostname


class HostGroup(models.Model):
    '''
    主机组,名字,主机
    '''
    name = models.CharField(max_length=64,unique=True)
    hosts = models.ManyToManyField(Host,blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    '''
    任务,时间
    '''
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id



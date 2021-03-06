# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-02 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_new', '0005_auto_20160601_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('view_customer_list', '可以查看客户列表'), ('view_customer_info', '可以查看客户详情'), ('edit_own_customer_info', '可以修改自己的客户信息'), ('view_course_list', '可以查看课程列表'), ('view_course_info', '可以查看课程详情'), ('edit_own_course_info', '可以修改课程信息'), ('view_class_list', '可以查看班级列表'), ('view_class_info', '可以查看班级详情'), ('edit_own_class_info', '可以修改班级信息'), ('view_school_list', '可以查看校区列表'), ('view_school_info', '可以查看校区详情'), ('edit_own_school_info', '可以修改校区信息'))},
        ),
        migrations.AddField(
            model_name='role',
            name='member',
            field=models.ManyToManyField(to='crm_new.UserProfile'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-01 02:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_new', '0004_auto_20160601_0257'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('view_customer_list', '可以查看客户列表'), ('view_customer_info', '可以查看客户详情'), ('edit_own_customer_info', '可以修改自己的客户信息'), ('view_course_list', '可以查看课程列表'), ('view_course_info', '可以查看课程详情'), ('edit_own_course_info', '可以修改课程信息'))},
        ),
    ]

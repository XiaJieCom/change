# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-11 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webchat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webgroup',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_webgroup_friends_+', to='webchat.WebGroup'),
        ),
    ]
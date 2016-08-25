# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-30 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=128, unique=True)),
                ('key', models.TextField()),
                ('status', models.SmallIntegerField(choices=[(0, 'Waiting Approval'), (1, 'Accepted'), (2, 'Rejected')], default=0)),
                ('os_type', models.CharField(choices=[('redhat', 'RedHat\\CentOS'), ('ubuntu', 'Ubuntu'), ('suse', 'SUSE'), ('windows', 'Windows')], default='redhat', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('hosts', models.ManyToManyField(blank=True, to='arya.Host')),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-09 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mass', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['c_time'], 'verbose_name': '用户表', 'verbose_name_plural': '用户数据'},
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=256, verbose_name='密码'),
        ),
    ]

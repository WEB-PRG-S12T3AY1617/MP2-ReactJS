# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0012_auto_20170726_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=64),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0020_auto_20170727_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='course_name',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]

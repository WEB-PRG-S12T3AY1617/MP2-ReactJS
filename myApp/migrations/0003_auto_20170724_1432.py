# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_auto_20170724_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0015_auto_20170726_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.User'),
        ),
    ]

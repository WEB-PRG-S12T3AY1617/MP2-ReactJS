# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 11:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0026_auto_20170815_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='hey',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='item',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='username',
        ),
    ]

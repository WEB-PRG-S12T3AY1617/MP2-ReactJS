# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 02:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0018_auto_20170726_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='username',
            new_name='post_username',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='user_username',
        ),
    ]

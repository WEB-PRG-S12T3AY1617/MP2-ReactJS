# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 14:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='thumbnail_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='thumbnail_image',
            new_name='image',
        ),
    ]

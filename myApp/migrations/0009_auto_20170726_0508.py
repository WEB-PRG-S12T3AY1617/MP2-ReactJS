# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 05:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_auto_20170725_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Post'),
        ),
        migrations.AlterField(
            model_name='item',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.User'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='myApp/static/myApp/Images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.User'),
        ),
    ]

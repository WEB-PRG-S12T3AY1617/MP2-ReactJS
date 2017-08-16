# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_auto_20170726_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type1',
            field=models.CharField(choices=[('0', 'Office'), ('1', 'Academic')], default='office', max_length=8),
        ),
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=8),
        ),
    ]

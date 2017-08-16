# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 15:45
from __future__ import unicode_literals

from django.db import migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_remove_item_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=tagging.fields.TagField(blank=True, max_length=255),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    degree_program = models.CharField(max_length=128)

class Post(models.Model):
    username = models.CharField(max_length=32)
    item_name = models.CharField(max_length=128)
    thumb_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    tags = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    
class Item(models.Model):
    quantity = models.PositiveSmallIntegerField()
    #condition = models.
    #if self.
    thumb_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    tags = models.CharField(max_length=128)
    username = models.CharField(max_length=32)
    
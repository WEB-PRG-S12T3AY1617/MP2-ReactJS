# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import User, Post, Item

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Item)

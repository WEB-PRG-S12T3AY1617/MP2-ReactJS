# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from tagging.fields import TagField
from tagging.models import Tag
from django.contrib.auth.models import User

# Create your models here.
CONDITION_CHOICES = (
	('0', '0'),
	('1', '1'),
	('2', '2'),
	('3', '3'),
	('4', '4'),
	('5', '5'),
	('6', '6'),
	('7', '7'),
	('8', '8'),
	('9', '9'),
	('10', '10'),
)

TYPE1_CHOICES = (
	('0', 'Office'),
	('1', 'Academic'), 
)

OFFER_CHOICES = (
	('0', 'exchange'),
	('1', 'purchase'),
)

Degree_Program_or_Office = models.CharField(max_length=128, default='')
Degree_Program_or_Office.contribute_to_class(User,'Degree_Program_or_Office')

class Post(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	item_name = models.CharField(max_length=128)
	image = models.FileField(upload_to='myApp/static/myApp/Images')
	tags = TagField()
	created = models.DateTimeField(auto_now_add=True, null=True)
	modified = models.DateTimeField(auto_now=True, null=True)
	quantity = models.PositiveSmallIntegerField(default=1)
	condition = models.CharField(max_length=8, choices=CONDITION_CHOICES, default='0') 
	type1 = models.CharField(max_length=8, choices=TYPE1_CHOICES, default='office') 
	course_name = models.CharField(max_length=32, default="N/A")
	
	def __str__(self):
		return self.item_name

class Offer(models.Model):
	item = models.ForeignKey(Post, on_delete=models.CASCADE, default=1, related_name='itemBuy')
	item2 = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='itemOffer', null=True, blank=True)
	userOffer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	offer_type = models.CharField(max_length=15, choices = OFFER_CHOICES, default = 'purchase')
	bid = models.FloatField(default=0.0)
	reason = models.TextField(max_length=128, default="N/A")
	accept = models.BooleanField(default=False)
	reject = models.BooleanField(default=False)
	
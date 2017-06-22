# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def validate(self, data):
		errors = []
		if len(data) < 8:
			errors.append("Username must be longer than 8 characters")
		elif len(data) > 24:
			errors.append("username must be shorter than 24 characters")
		if len(errors) == 0:
			user = User.objects.create(username=data)
			return user
		else:
			return errors

class User(models.Model):
	username = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

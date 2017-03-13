from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email_add = models.CharField(max_length=255, unique=True)
	pw_has = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

from __future__ import unicode_literals
import re, bcrypt
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name = re.compile(r'^[a-zA-Z]')

class UserManager(models.Manager):
	def UsersValidate(self, request):
		errors=[]
		if len(request.POST['first_name'])<2:
			errors.append("First Name Needs More Characters")
		elif not name.match(request.POST['first_name']):
			errors.append("No Numbers Allowed in First Name")
		if len(request.POST['last_name'])<2:
			errors.append("Last Name Needs More Characters")
		elif not name.match(request.POST['last_name']):
			errors.append("No Numbers Allowed in Last Name")
		if not EMAIL_REGEX.match(request.POST['email_add']):
			errors.append("Email is Not Valid")
		if len(request.POST['password']) < 9:
			errors.append("Password Needs to be 9 Characters or More!")
		if request.POST['password'] != request.POST['confirm']:
			errors.append("Passwords Do Not Match!")
		return errors

	def Register(self, request):
		password = request.POST['password']
		hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_add=request.POST['email_add'], pw_has=hashed)

	def Login(self, request):
		user = Users.objects.filter(email_add = request.POST['username'])
		if len(user)>0:
			user[0].pw_has
		incPassword = request.POST['password2']
		storedPassword = Users.objects.only('pw_has').get(email_add=request.POST['username']).pw_has
		if bcrypt.hashpw(incPassword.encode(), storedPassword.encode())  == storedPassword:
			print "Yay"
		else:
			print "Nope!"
			

class Users(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email_add = models.CharField(max_length=255, unique=True)
	pw_has = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects=UserManager()

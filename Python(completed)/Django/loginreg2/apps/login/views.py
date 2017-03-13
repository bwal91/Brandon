from django.shortcuts import render, redirect
from .models import Users
import re, bcrypt
from django.contrib import messages

EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name = re.compile(r'^[a-zA-Z]')


def index(request):
	
	return render(request, 'login/index.html')

def login(request):
	Users.objects.Login(request)
	request.session['id']=Users.objects.only('id').get(email_add=request.POST['username']).id
	request.session['name']=Users.objects.only('first_name').get(id=request.session['id']).first_name
		
	return redirect('/success')

def register(request):
	errors=Users.objects.UsersValidate(request)
	if not errors == []:
		for error in errors:
			messages.info(request, error)
	else:
		Users.objects.Register(request)
		return redirect('/success')
	return redirect('/success')
	
def success(request):
	
	return render(request, 'login/success.html')

def goback(request):
	if 'name' in request.session:	
		del request.session['name']
	return redirect('/')
from django.shortcuts import render, redirect
from .models import Users
from django.core.urlresolvers import reverse
import re, bcrypt
from django.contrib import messages


EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name = re.compile(r'^[a-zA-Z]')


def index(request):
	return render(request, 'login/index.html')

def login(request):
    if request.method=="POST":
    log=Registrations.objects.Login(request)
    print log
    if not log ==[]:
        for error in log:
            messages.info(request, error)
        return redirect(reverse('login:index'))
    else:
        request.session['id']=Registrations.objects.only('id').get(email_add=request.POST['username']).id
        request.session['username']=Registrations.objects.only('first_name').get(id=request.session['id']).first_name
        return redirect('/')

def register(request):
	errors=Users.objects.UsersValidate(request)
	if not errors == []:
		for error in errors:
			messages.info(request, error)
		return redirect(reverse('login:index'))
	else:
		Users.objects.Register(request)
		return redirect(reverse('loginApp:my_success'))
	return redirect(reverse('loginApp:my_success'))
	
def success(request):
	
	return render(request, 'login/success.html')

def goback(request):
	if 'name' in request.session:	
		del request.session['name']
	return redirect(reverse('loginApp:my_index'))
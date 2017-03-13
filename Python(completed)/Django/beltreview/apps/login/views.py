from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Registrations
import re, bcrypt
EMAIL_REGEX=re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name=re.compile(r'^[a-zA-Z]')

#rendering html page
def index(request):
    return render(request, 'login/index.html')

#Login validation
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
            request.session['name']=Registrations.objects.only('first_name').get(id=request.session['id']).first_name
            return redirect(reverse('books:index'))

#Registering person
def register(request):
    errors=Registrations.objects.RegistrationValidation(request)
    # print errors
    if not errors ==[]:
        for error in errors:
            messages.info(request, error)
        return redirect(reverse('login:index'))
    else:
        newUser=Registrations.objects.Register(request)
        request.session['name']=request.POST['first_name']
        return redirect(reverse('books:index'))
    return redirect(reverse('login:index'))


# def clear(request):
#     if request.method=="POST":
#         del request.session['username']
#         del request.session['id']
#         return redirect(reverse('loginApp:my_index'))

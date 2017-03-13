from django.shortcuts import render, redirect
from .models import Users
import re, bcrypt
from django.contrib import messages

EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name = re.compile(r'^[a-zA-Z]')


def index(request):
	
	return render(request, 'login/index.html')

def login(request):
	if request.method == "POST":
		if len(Users.objects.filter(email_add=request.POST['username']))==1:
			incPassword = request.POST['password2']
			storedPassword = Users.objects.only('pw_has').get(email_add=request.POST['username']).pw_has
			if bcrypt.hashpw(incPassword.encode(), storedPassword.encode())  == storedPassword:
				request.session['id']=Users.objects.only('id').get(email_add=request.POST['username']).id
				request.session['name']=Users.objects.only('first_name').get(id=request.session['id']).first_name
				return redirect('/success')
		else:
			request.session['nomatch']="Email and Password Do NOT Match or Do Not Exist!"
			return redirect('/')
		
def register(request):
	if request.method == "POST":
		error = 0
		if len(request.POST['first_name'])<2:
			error += 1
			messages.info(request, "First Name Needs More Charecters")
		elif not name.match(request.POST['first_name']):
			error += 1
			messages.info(request, 'No Numbers Allowed in First Name')
		if len(request.POST['last_name'])<2:
			error += 1
			messages.info(request, 'Last Name Needs More Charecters')
		elif not name.match(request.POST['last_name']):
			error += 1
			messages.info(request, 'No Numbers Allowed in Last Name')
		if not EMAIL_REGEX.match(request.POST['email_add']):
			error +=1
			messages.info(request, 'Email is Not Valid')
		if len(request.POST['password']) < 9:
			error += 1
			messages.info(request, 'Password needs to be 9 charecters or more!')
		if request.POST['password'] != request.POST['confirm']:
			error += 1
			messages.info(request, 'Passwords Do Not Match!')
	
		if error == 0:
			password = request.POST['password']
			hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_add=request.POST['email_add'], pw_has=hashed)
			request.session['id']=Users.objects.only('id').get(email_add=request.POST['username']).id
			request.session['name']=Users.objects.only('first_name').get(id=request.session['id']).first_name
			return redirect('/success')

	return redirect('/')

def success(request):
	
	return render(request, 'login/success.html')

def goback(request):
	del request.session['name']
	del request.session['nomatch']
	return redirect('/')
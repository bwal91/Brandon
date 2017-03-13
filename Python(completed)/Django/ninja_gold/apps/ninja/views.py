from django.shortcuts import render, redirect
import random

def index(request):
	if not 'gold' in request.session:
		request.session['gold']=0
	if not 'res' in request.session:
		request.session['res']=0
	if not 'activities' in request.session:
		request.session['activities']=[]
	return render(request, 'ninja/index.html')


def gold(request):
	if request.method == "POST":
		if request.POST['building']=='farm':
			request.session['']=0
			request.session['res']=request.session['res']+random.randrange(10,21)
			request.session['gold']=request.session['gold']+request.session['res']
			request.session['where']='Farm'
		elif request.POST['building']=='cave':
			request.session['res']=0
			request.session['res']=request.session['res']+random.randrange(-4, 11)
			request.session['gold']=request.session['gold']+request.session['res']
			request.session['where']='Caves'
		elif request.POST['building']=='house':
			request.session['res']=0
			request.session['res']=request.session['res']+random.randrange(9, 21)
			request.session['gold']=request.session['gold']+request.session['res']
			request.session['where']='House'
		elif request.POST['building']=='casino':
			request.session['res']=0
			request.session['res']=request.session['res']+random.randrange(-51, 51)
			request.session['gold']=request.session['gold']+request.session['res']
			request.session['where']='Casino'
	request.session['activities'].append('You earned ' + str(request.session['res'])+ ' gold from the '+ str(request.session['where'])+'!')
	return redirect ('/')

def reset(request):
	if request.method == "POST":
		del request.session['gold']
		del request.session['res']
		del request.session['activities']
	return redirect('/')

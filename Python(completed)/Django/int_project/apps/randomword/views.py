from django.shortcuts import render, redirect
import random
import string
from django.core.urlresolvers import reverse

def index(request):
	if 'counter' not in request.session:
		request.session['counter']=1
	
	return render(request, 'randomword/index.html')



def generate(request):
	passkey = ''
	this = 0
	if request.method == "POST":
		this += 1
		request.session['this']=this
		for x in range(10):
			passkey += passkey.join(random.choice(string.ascii_uppercase))
			request.session['name']=passkey
		request.session['counter'] += 1
		return redirect(reverse('randomApp:my_index'))
	else:
		return redirect(reverse('randomApp:my_index'))
	


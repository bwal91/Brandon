from django.shortcuts import render, redirect


def index(request):
	if 'counter' not in request.session:
		request.session['counter']=1
	
	return render(request, 'survey/index.html')

def survey(request):
	if request.method == "POST":
		request.session['firstname']=request.POST['firstname']
		request.session['location']=request.POST['location']
		request.session['language']=request.POST['language']
		request.session['com']=request.POST['com']
		request.session['counter'] += 1
	return redirect('/result')

def result(request):
	
	return render(request, 'survey/result.html')
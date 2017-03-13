from django.shortcuts import render

def index(request):
	

	return render(request, 'ninja/welcome.html')

def ninjas(request):

	return render(request, 'ninja/images.html')

def person(request, person):
	context = {
	'image': person
	}
	return render(request, "ninja/result.html", context)
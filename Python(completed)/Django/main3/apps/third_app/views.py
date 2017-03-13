from django.shortcuts import render
from .models import People

def index(request):
	People.objects.create(first_name="Brandon", last_name="Walter")
	people = People.objects.all()
	print (people)

	return render(request, 'third_app/index.html')
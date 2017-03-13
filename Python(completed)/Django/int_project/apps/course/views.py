from django.shortcuts import render, redirect
from .models import Courses
from django.core.urlresolvers import reverse

def index(request):
	context = {
	"courses": Courses.objects.all()
	}

	return render(request, 'course/index.html', context)

def addCourse(request):
	if request.method == "POST":
		Courses.objects.create(name=request.POST['coursename'], description=request.POST['desc'])
	return redirect(reverse('courseApp:my_index'))

def destroy(request, id):
	context = {
	"courses": Courses.objects.filter(id=id),
	"id": id
	}

	return render(request, 'course/verify.html', context)

def delete(request, id):
	if request.method == "POST":
		Courses.objects.filter(id=id).delete()
	return redirect(reverse('courseApp:my_index'))

def no(request, id):
	return redirect(reverse('courseApp:my_index'))
from django.shortcuts import render, redirect
from .models import Books, Reviews
from ..login.models import Registrations
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Count
import re

def index(request):
	context = {
	"reviews": Reviews.objects.all(),
	"books": Books.objects.all(),
	"stars": Reviews.objects.only('rating')
	}
	
	return render(request, 'belt/index.html', context)

def add(request):

	return render(request, 'belt/add.html')

def bookadd(request):
	errors=Books.objects.BookValidation(request)
	if not errors == []:
		for error in errors:
			message.info(request, error)
		return redirect('/add')
	else:
		Books.objects.AddBook(request)
		request.session['bookid']=Books.objects.only('id').get(book_title=request.POST['title']).id
		Reviews.objects.AddReview(request)
		return redirect(reverse('books:index'))


def edit(request, id):
	context = {
	"reviews": Reviews.objects.filter(book__id=id),
	"stars": Reviews.objects.filter(book__id=id).only('rating'),
	}
	request.session['booktitle']=Books.objects.only('book_title').get(id=id).book_title
	request.session['bookauthor']=Books.objects.only('author').get(id=id).author
	return render(request, 'belt/edit.html', context)


def reviewadd(request, id):
	errors=Reviews.objects.ReviewValidation(request)
	if not errors == []:
		for error in errors:
			message.info(request, error)
		return redirect(reverse('books:index'))
	else:
		request.session['bookid']=id
		Reviews.objects.AddReview(request)
		return redirect(reverse('books:index'))

def users(request, id):
	context = {
	"reviews": Reviews.objects.filter(users__id=id),
	"count": Reviews.objects.filter(users__id=id).annotate(count=Count('reviews')),
	}
	
	return render(request, 'belt/users.html', context)

def logout(request):
	for sesskey in request.session.keys():
		del request.session[sesskey]
	return redirect(reverse('login:index'))












from __future__ import unicode_literals
from django.db import models
from ..login.models import Registrations

class ReviewManager(models.Manager):
	def ReviewValidation(self, request):
		errors=[]
		if len(request.POST['review'])<5:
			errors.append("Please Enter a Review")
		return errors

	def AddReview(self, request):

		Reviews.objects.create(reviews=request.POST['review'], rating=request.POST['rating'], users=Registrations.objects.get(id=request.session['id']), book=Books.objects.get(id=request.session['bookid']))

class BookManager(models.Manager):
	def BookValidation(self, request):
		errors = []
		if len(request.POST['title'])<2:
			errors.append("Pleast Enter a Title")
		if len(request.POST['authorname'])<2:
			errors.append("Please Enter an Author")
		if len(request.POST['review'])<5:
			errors.append("Please Enter a Review")
		
		return errors



	def AddBook(self, request):
		if len(request.POST['choseauthor'])<1:
			author=request.POST['authorname']
		Books.objects.create(book_title=request.POST['title'], author=author)
		

class Books(models.Model):
    book_title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=BookManager()

class Reviews(models.Model):
	reviews = models.TextField()
	rating = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	users = models.ForeignKey(Registrations)
	book = models.ForeignKey(Books)
	objects=ReviewManager()




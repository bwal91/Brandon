from django.conf.urls import url
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^add/course$', views.addCourse),
	url(r'^courses/destroy/(?P<id>\d+)/$', views.destroy),
	url(r'^courses/destroy/(?P<id>\d+)/delete$', views.delete),
	url(r'^courses/destroy/(?P<id>\d+)/no$', views.no)
]
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^images$', views.ninjas),
	url(r'^ninjas/(?P<person>\w+)$', views.person)
	
]
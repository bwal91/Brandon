from django.conf.urls import url
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name='my_index'),
	url(r'^process_money$', views.gold, name='my_money'),
	url(r'^reset$', views.reset, name='my_reset'),
	
]
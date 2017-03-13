from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add$', views.add, name='add'),
	url(r'^addbook$', views.bookadd),
	url(r'^logout$', views.logout),
	url(r'^title/(?P<id>\d+)$', views.edit, name='edit'),
	url(r'^title/addreview/(?P<id>\d+)$', views.reviewadd, name='addreview'),
	url(r'^users/(?P<id>\d+)$', views.users, name='users'),
	

]
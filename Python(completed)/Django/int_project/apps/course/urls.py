from django.conf.urls import url
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name='my_index'),
	url(r'^add/course$', views.addCourse, name='my_addcourse'),
	url(r'^courses/destroy/(?P<id>\d+)/$', views.destroy, name='my_destroy'),
	url(r'^courses/destroy/(?P<id>\d+)/delete$', views.delete, name='my_delete'),
	url(r'^courses/destroy/(?P<id>\d+)/no$', views.no, name='my_no')
]
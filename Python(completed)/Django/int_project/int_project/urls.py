"""int_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.login.urls', namespace='loginApp')),
    url(r'^project/', include('apps.project.urls', namespace='projectApp')),
    url(r'^goldApp/', include('apps.ninja.urls', namespace='goldApp')),
    url(r'^courseApp/', include('apps.course.urls', namespace='courseApp')),
    url(r'^randomApp/', include('apps.randomword.urls', namespace='randomApp')),
    url(r'^timeApp/', include('apps.timedisplay.urls', namespace='timeApp')),
    
]

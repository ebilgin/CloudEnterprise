from django.conf.urls import patterns, include, url
from django.contrib import admin
from account.views import *

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
    
)

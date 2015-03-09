from django.conf.urls import patterns, include, url
from django.contrib import admin
from login.views import *

urlpatterns = patterns('',
        
    url(r'^$', logout_page, name='index'),
    url(r'^logout/$', logout_page, name='logout_page'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register, name='register'),
    url(r'^registration/success/$', register_success,"register_success"),
    url(r'^home/$', home),
)

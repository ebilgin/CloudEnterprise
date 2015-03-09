from django.conf.urls import patterns, include, url
from django.contrib import admin
from login.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'erp1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   # url(r'^$', 'erp1.views.home', name='home'),
   # url(r'^a_inv/', include('a_inv.urls')),
   # url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls', namespace="account")),
    #===========================================================================
    # url(r'^$', 'django.contrib.auth.views.login'),
    # url(r'^logout/$', logout_page),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    # url(r'^register/$', register),
    # url(r'^registration/success/$', register_success,"register_success"),
    # url(r'^home/$', home),
    #===========================================================================
)

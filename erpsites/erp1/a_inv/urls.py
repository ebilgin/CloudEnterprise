from django.conf.urls import patterns, url

from a_inv import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^(?P<idn>\d+)/$', views.supplier_view, name='supplier_view'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    
)
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'deafgrandpa.views.index', name='index'),
    url(r'^say$', 'deafgrandpa.views.say', name='say'),
)

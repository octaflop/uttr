# encoding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('profiles.views.home',
    url(r'^$', 'index', name='home'),
)

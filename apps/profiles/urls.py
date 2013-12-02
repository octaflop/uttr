# encoding: utf-8

from django.conf.urls import patterns, include, url

patterns = patterns('profiles.views.home.index',
    url(r'^$', 'profile_home', name='home'),
)

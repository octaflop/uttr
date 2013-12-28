#encoding: utf-8
from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns('pages.views',
    url(r'^about/$', 'about', name='about'),
    url(r'^conductcode/$', 'code_of_conduct', name='code'),
)
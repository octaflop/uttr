#encoding: utf-8
from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('library.views',
    url(r'^(?P<bid>[\w-]+)/$', 'resource_view', name='view'),
    url(r'^byslug/(?P<slug>[\w-]+)/$', 'resource_view_by_slug', name='view_by_slug'),
    url(r'^$', 'resource_list', name='list'),
)
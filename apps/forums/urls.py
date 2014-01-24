#encoding: utf-8
from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('forums.views',
    url(r'^(?P<bid>[\w-]+)/$', 'topic_view', name='view'),
    url(r'^byslug/(?P<slug>[\w-]+)/$', 'topic_view_by_slug', name='view_by_slug'),
    url(r'^$', 'topic_list', name='list'),
)
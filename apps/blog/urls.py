#encoding: utf-8
from django.conf import settings
from django.conf.urls import patterns, include, url

managepatterns = patterns('blog.views.manage',
	url(r'^create$', 'create', name='create'),
)

urlpatterns = patterns('',
	url(r'^manage/', include(managepatterns, namespace='manage'))
)
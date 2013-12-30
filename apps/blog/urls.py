#encoding: utf-8
from django.conf import settings
from django.conf.urls import patterns, include, url

managepatterns = patterns('blog.views.manage',
    url(r'^create$', 'create', name='create'),
)

librarypatterns = patterns('blog.views.list',
    url(r'^$', 'library_list', name='index'),
    url(r'^(?P<id>\d+)$', 'library_entry', name='view'),
)

discussionpatterns = patterns('blog.views.list',
    url(r'^$', 'discussion_list', name='index'),
    url(r'^(?P<id>\d+)$', 'discussion_entry', name='view'),
)

pmpatterns = patterns('blog.views.pm',
    url(r'^create$', 'create', name='create'),
    # For now, use the admin to view
    # url(r'^$', 'pm_list', name='index'),
    # url(r'^(?P<id>\d+)$', 'create', name='view'),
)

urlpatterns = patterns('',
    url(r'^manage/', include(managepatterns, namespace='manage')),
    url(r'^library/', include(librarypatterns, namespace='library')),
    url(r'^discussion/', include(discussionpatterns, namespace='discussion')),
    url(r'^messages/', include(pmpatterns, namespace='pm'))
)
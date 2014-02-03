#encoding: utf-8
from django.conf import settings
from django.conf.urls import patterns, include, url

from forums.views.api import reply_resource

apipatterns = patterns('forums.views.api',
    url(r'v2/', include(reply_resource.urls)),
    url(r'reply_topic/(?P<topic_id>[\w-]+)/$', 'reply_to_topic', name='reply_topic'),
    url(r'reply/(?P<parent_id>[\w-]+)/$', 'reply_to_parent', name='reply')
)

managepatterns = patterns('forums.views.manage',
    url(r'^create$', 'topic_create', name='create'),
    url(r'^edit/(?P<bid>[\w-]+)/$', 'topic_edit', name='edit'),
)

urlpatterns = patterns('forums.views.home',
    url(r'^api/', include(apipatterns, namespace='api')),
    url(r'^manage/', include(managepatterns, namespace='manage')),
    url(r'^(?P<bid>[\w-]+)/$', 'topic_view', name='view'),
    url(r'^byslug/(?P<slug>[\w-]+)/$', 'topic_view_by_slug', name='view_by_slug'),
    url(r'^$', 'topic_list', name='list'),
)
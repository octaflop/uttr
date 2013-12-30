#encoding: utf-8
from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'profiles.views.home.login_view', name='home'),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^pages/', include('pages.urls', namespace='pages')),

    # 3rd party urls
    url(r'^ckeditor/', include('uttr.ckeditor_urls')),
    url(r'^search/', include('haystack.urls', namespace='search')),

    # admin urls
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

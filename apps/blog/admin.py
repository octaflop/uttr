# encoding: utf-8

from django.contrib import admin
from blog.models import BlogPost, Source

class BlogPostAdmin(admin.ModelAdmin):
    pass

class SourceAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Source, SourceAdmin)

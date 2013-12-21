# encoding: utf-8

from django.contrib import admin
from blog.models import BlogPost, Source, ModNotes

class BlogPostAdmin(admin.ModelAdmin):
    pass

class SourceAdmin(admin.ModelAdmin):
    pass

class ModNotesAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(ModNotes, ModNotesAdmin)

# encoding: utf-8


from django import forms
from django.contrib import admin

from ckeditor.widgets import CKEditorWidget

from blog.models import BlogPost, Source, ModNotes

class BlogPostAdminForm(forms.ModelForm):
    entry = forms.CharField(widget=CKEditorWidget())
    draft = forms.CharField(widget=CKEditorWidget())
    mod_notes = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}
    form = BlogPostAdminForm

class SourceAdmin(admin.ModelAdmin):
    pass

class ModNotesAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(ModNotes, ModNotesAdmin)

# encoding: utf-8

from django import forms
from django.contrib import admin

from ckeditor.widgets import CKEditorWidget

from library.models import Resource

class ResourceAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Resource

class ResourceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}
    form = ResourceAdminForm

admin.site.register(Resource, ResourceAdmin)

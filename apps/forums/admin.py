# encoding: utf-8

from django import forms
from django.contrib import admin

from ckeditor.widgets import CKEditorWidget

from forums.models import Topic, Reply

class TopicAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Topic


class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}
    form = TopicAdminForm


class ReplyAdmin(admin.ModelAdmin):
    class Meta:
        model = Reply


admin.site.register(Topic, TopicAdmin)
admin.site.register(Reply, ReplyAdmin)

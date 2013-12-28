#encoding: utf-8

from django.contrib import admin

from pages.models import Announcement, File

class AnnouncementAdmin(admin.ModelAdmin):
    models = Announcement

class FileAdmin(admin.ModelAdmin):
    models = File

admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(File, FileAdmin)
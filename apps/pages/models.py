# encoding: utf-8

from django.db import models


class Announcement(models.Model):
    """
    A basic admin Announcement shown on all pages
    """
    entry = models.TextField()


class File(models.Model):
    """
    A basic file-upload field
    """
    uttr_file = models.FileField(upload_to='pages/files')

    def __unicode__(self):
        return self.uttr_file.file.name

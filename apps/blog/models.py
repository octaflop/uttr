# encoding: utf-8
# models.py

from django.db import models
from uttr.models.mixins import TimestampMixin

class BlogPost(TimestampMixin):
    title = models.CharField(max_length=250)
    author = models.ForeignKey('profiles.UttrUser')
    entry = models.TextField()


class Source(models.Model):
    url = models.URLField(blank=True)
    author = models.CharField(max_length=250, blank=True)

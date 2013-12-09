# encoding: utf-8
# models.py

from django.db import models
from uttr.models.mixins import TimestampMixin

from profiles.models import UttrUser
from polls.models import Poll

class BlogPost(TimestampMixin):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(UttrUser)
    entry = models.TextField()
    tags = models.CharField(max_length=500, blank=True)
    publish_date = models.DateTimeField(blank=True, null=True)

    source = models.ForeignKey("Source", blank=True, null=True)
    poll = models.ForeignKey(Poll, blank=True, null=True)


class Source(models.Model):
    url = models.URLField(blank=True)
    author = models.CharField(max_length=250, blank=True)


class ModNotes(TimestampMixin):
    post = models.ForeignKey(BlogPost)
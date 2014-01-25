#encoding: utf-8

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.http import int_to_base36

from uttr.models.mixins import TimestampMixin


class Resource(TimestampMixin):
    """
    A topic heads off each forum thread
    only admins can create a topic
    """
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, default='', unique=True)
    content = models.TextField()
    link = models.URLField(blank=True, help_text="A URL link to the resource.\
         If available. Won't appear if it's not filled in")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library:view', kwargs=dict(bid=int_to_base36(self.id)))

    @property
    def latest(self):
        try:
            try:
                return self.reply_set.filter(status='posted').order_by('created_at')[0].entry
            except IndexError:
                return
        except KeyError:
            return

    @property
    def reply_length(self):
        return len(self.reply_set.filter(status='posted'))


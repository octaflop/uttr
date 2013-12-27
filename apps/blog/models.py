# encoding: utf-8
# models.py

from django.db import models
from django.core.urlresolvers import reverse
from uttr.models.mixins import TimestampMixin

from taggit.managers import TaggableManager

from profiles.models import UttrUser
from polls.models import Poll

POST_STATUS = (
    ('draft', 'Private'),
    ('posted', 'Posted'),
    ('redacted', 'Redacted'),
)

POST_TYPE = (
    ('lib', 'Library'),
    ('disc', 'Discussion'),
    ('pm', 'Private Message'),
)

class BlogPost(TimestampMixin):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=40, default='')
    author = models.ForeignKey(UttrUser)
    entry = models.TextField(blank=True)
    draft = models.TextField()
    mod_notes = models.TextField(blank=True)
    tags = TaggableManager()
    publish_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(choices=POST_STATUS, max_length=10, default='draft')
    post_type = models.CharField(choices=POST_TYPE, max_length=10, default='disc')

    is_poll = models.BooleanField(default=False)

    poll = models.ForeignKey(Poll, blank=True, null=True)
    parent_post = models.ForeignKey('self', blank=True, null=True)

    def get_absolute_url(self):
        if self.post_type == 'lib':
            return reverse('blog:library:view', kwargs={'id': str(self.id)})
        elif self.post_type == 'disc':
            return reverse('blog:discussion:view', kwargs={'id': str(self.id)})
        elif self.post_type == 'pm':
            return reverse('blog:pm:view', kwargs={'id': str(self.id)})
        return

    def __unicode__(self):
        return self.title

    @property
    def is_child(self):
        if self.parent_post:
            return True
        return False

    @property
    def replys_to(self):
        if self.parent_post:
            return parent_post
        return False


class Source(models.Model):
    url = models.URLField(blank=True)
    author = models.CharField(max_length=250, blank=True)

    def __unicode__(self):
        return "%s (%s)" % (self.author, self.url[:35])


class ModNotes(TimestampMixin):
    post = models.ForeignKey(BlogPost)
    notes = models.TextField(blank=True, null=True)
    mod = models.ForeignKey('profiles.UttrUser', blank=True, null=True)

    class Meta:
        verbose_name_plural = u'Mod Notes'
        verbose_name = u'Mod Note'

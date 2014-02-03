#encoding: utf-8

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.http import int_to_base36

from uttr.models.mixins import TimestampMixin

from taggit.managers import TaggableManager

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

class Topic(TimestampMixin):
    """
    A topic heads off each forum thread
    only admins can create a topic
    """
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, default='', unique=True)
    content = models.TextField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forums:view', kwargs=dict(bid=int_to_base36(self.id)))

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
        
    @property
    def bid(self):
        return int_to_base36(self.id)


class Reply(TimestampMixin):
    """
    A reply to a Topic 
    can also reply to any other 'reply'
    if it's replying to a reply, then it's a child post
    """
    author = models.ForeignKey('profiles.UttrUser')
    # content
    draft = models.TextField()
    entry = models.TextField(blank=True)
    mod_notes = models.TextField(blank=True)
    # topic that we're replying to
    topic = models.ForeignKey(Topic)
    # metadata
    tags = TaggableManager(blank=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    # categorization
    status = models.CharField(choices=POST_STATUS, max_length=10, default='draft')
    post_type = models.CharField(choices=POST_TYPE, max_length=10, default='disc')
    # poll relationship
    is_poll = models.BooleanField(default=False)
    # TODO: relate to poll. this might take place in another model
    # poll = models.ForeignKey('polls.Poll', blank=True, null=True)
    # reply modeling — determines the reply position; esp if replying to another post
    # if True and not None, then it's a response (see method below)
    parent_post = models.ForeignKey('self', blank=True, null=True)


    def __unicode__(self):
        return "%s by %s in response to %s" % (self.bid, self.author, self.topic.title)

    @property
    def bid(self):
        return int_to_base36(self.id)

# encoding: utf-8
# models.py


from django.db import models
from uttr.models.mixins import TimestampMixin

from profiles.models import UttrUser

class PollQuestion(TimestampMixin):
    question = models.TextField()

    def __unicode__(self):
        return "%s" % self.question


class PollAnswer(TimestampMixin):
    answer = models.TextField()


class PollVote(TimestampMixin):
    voter = models.ForeignKey(UttrUser)


class Poll(TimestampMixin):
    question = models.ForeignKey(PollQuestion)
    answers = models.ManyToManyField(PollAnswer, blank=True, null=True)
    votes = models.ManyToManyField(PollVote, blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.question.question)


class PostPoll(TimestampMixin):
    """
    Post poll is directly related to a post and has static answers
    """
    VOTE_CHOICES = (
        ("unread", "Unread"),
        ("agree", "Agree"),
        ("neutral", "Neutral"),
        ("disagree", "Disagree"),
        ("postpone", "Post Pone"),
        ("none", "None"),
    )
    answeree = models.ForeignKey("profiles.UttrUser")
    entry = models.ForeignKey("blog.BlogPost")
    answer = models.CharField(max_length=8, choices=VOTE_CHOICES, default='unread')

    def __unicode__(self):
        return u"%s answered %s on %s" % (self.answeree.first_name, self.answer, self.entry)


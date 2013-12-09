# encoding: utf-8
# models.py


from django.db import models
from uttr.models.mixins import TimestampMixin


class PollQuestion(TimestampMixin):
    question = models.TextField()

    def __unicode__(self):
        return "%s" % self.question


class PollAnswer(TimestampMixin):
    answer = models.TextField()


class PollVote(TimestampMixin):
    voter = models.ForeignKey('profiles.UttrUser')


class Poll(TimestampMixin):
    question = models.ForeignKey(PollQuestion)
    answers = models.ManyToManyField(PollAnswer, blank=True, null=True)
    votes = models.ManyToManyField(PollVote, blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.question.question)

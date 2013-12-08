# encoding: utf-8
# models.py


from django.db import models
from uttr.models.mixins import TimestampMixin


class PollQuestion(TimestampMixin):
    pass


class PollVote(TimestampMixin):
    pass


class Poll(TimestampMixin):
    pass
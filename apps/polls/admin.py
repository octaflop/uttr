# encoding: utf-8
# admin.py

from django.contrib import admin

from polls.models import PollQuestion, PollAnswer, Poll

class PollQuestionInline(admin.TabularInline):
    model = PollQuestion


class PollAnswerInline(admin.TabularInline):
    model = PollAnswer


class PollAdmin(admin.ModelAdmin):
    model = Poll

admin.site.register(PollQuestion)
admin.site.register(PollAnswer)
admin.site.register(Poll, PollAdmin)

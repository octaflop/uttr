# encoding: utf-8
# api.py

from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.http import base36_to_int
from django.http import HttpResponse

from forums.models import Topic, Reply
from forums.forms import ReplyForm

from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization

"""
Various functions for AJAX/JS interaction
"""

class ReplyResource(ModelResource):
    class Meta:
        queryset = Reply.objects.all()
        resource_name = 'reply'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()

    def obj_create(self, bundle, **kwargs):
        return super(ReplyResource, self).obj_create(bundle, author=bundle.request.user)


reply_resource = ReplyResource()


def reply_to_topic(request, topic_id):
    """
    A direct reply to a topic
    """
    ctx = {}
    template_name = 'forums/api/reply_form.html'

    reply_form = ReplyForm()
    ctx['reply_form'] = reply_form
    ctx['topic_id'] = topic_id
    topic = Topic.objects.get(id=base36_to_int(topic_id))

    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        reply_form.topic = topic
        reply_form.author = request.user
        if reply_form.is_valid:
            reply = reply_form.save(commit=False)
            reply.author = request.user
            reply.topic = topic
            reply.save()
            messages.warning(request, "Thank you for your reply. It has been sent for moderation")
            return redirect(topic.get_absolute_url())

            # we might have to use a JS return
            # response = HttpResponse()
            # response.type = 'text/javascript'
            # response.write('Success!')
            # return response

    return render(request, template_name, ctx)


def reply_to_parent(request, parent_id):
    """
    Creates a form for sending replies
    Also creates a reply on POST
    Relies on jQuery's html-handling
    """
    ctx = {}
    template_name = 'forums/api/reply_to_parent.html'

    reply_form = ReplyForm()
    ctx['reply_form'] = reply_form
    ctx['parent_id'] = parent_id
    parent = Reply.objects.get(id=base36_to_int(parent_id))
    topic = parent.topic

    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        reply_form.topic = topic
        reply_form.author = request.user
        if reply_form.is_valid:
            reply = reply_form.save(commit=False)
            reply.author = request.user
            reply.topic = topic
            reply.parent = parent
            reply.status = 'posted'
            reply.entry = reply.draft
            reply.save()
            messages.warning(request, "Thank you for your reply. It has been sent for moderation")
            return redirect(topic.get_absolute_url())

    return render(request, template_name, ctx)


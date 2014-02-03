# encoding: utf-8
# api.py

from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization

from forums.models import Reply
from forums.forms import ReplyForm

from django.shortcuts import redirect, render

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

    ctx['reply_form'] = ReplyForm()
    ctx['topic_id'] = topic_id

    return render(request, template_name, ctx)


def reply_to_parent(request, parent_id):
    """
    Creates a form for sending replies
    Also creates a reply on POST
    Relies on jQuery's html-handling
    """
    ctx = {}
    template_name = 'forums/api/reply_form.html'

    ctx['reply_form'] = ReplyForm()
    ctx['parent_id'] = parent_id

    return render(request, template_name, ctx)


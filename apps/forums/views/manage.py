# encoding: utf-8

from django.shortcuts import render, redirect
from django.utils.http import base36_to_int, int_to_base36
from django.core.urlresolvers import reverse

from forums.models import Topic, Reply

def topic_create(request):
    ctx = {}
    template_name = 'forums/forums_list.html'

    topics = Topic.objects.all()
    ctx['topics'] = topics

    return render(request, template_name, ctx)

def topic_view_by_slug(request, slug):
    """
    redirects to bid-based view
    """
    topic = Topic.objects.get(slug=slug)
    return redirect(reverse('forums:view', kwargs={'bid': int_to_base36(topic.id)}))

def topic_edit(request, bid):
    """
    Edit the topic
    """
    ctx = {}
    template_name = 'forums/topic_view.html'

    topic = Topic.objects.get(id=base36_to_int(bid))
    ctx['topic'] = topic

    ctx['replies'] = Reply.objects.filter(topic=topic, status='posted')

    return render(request, template_name, ctx)

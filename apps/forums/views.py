# encoding: utf-8

from django.shortcuts import render

from forums.models import Topic

def topic_list(request):
    ctx = {}
    template_name = 'forums/forums_list.html'

    topics = Topic.objects.all()
    ctx['topics'] = topics

    return render(request, template_name, ctx)

def view_topic(request, slug):
    ctx = {}
    template_name = 'forums/topic_view.html'

    topic = Topic.objects.get(slug=slug)
    ctx['topic'] = topic

    return render(request, template_name, ctx)

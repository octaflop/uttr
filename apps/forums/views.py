# encoding: utf-8

from django.shortcuts import render

from forums.models import Topic, Reply

def topic_list(request):
    ctx = {}
    template_name = 'forums/forums_list.html'

    topics = Topic.objects.all()
    ctx['topics'] = topics

    return render(request, template_name, ctx)

def topic_view(request, slug):
    """
    List the topic at the top and disply replies
    """
    ctx = {}
    template_name = 'forums/topic_view.html'

    topic = Topic.objects.get(slug=slug)
    ctx['topic'] = topic

    ctx['replies'] = Reply.objects.filter(topic__slug=slug, status='posted')

    return render(request, template_name, ctx)

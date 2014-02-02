# encoding: utf-8

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.http import base36_to_int, int_to_base36
from django.core.urlresolvers import reverse

from forums.models import Topic, Reply
from forums.forms import TopicForm


@staff_member_required
def topic_create(request):
    ctx = {}
    template_name = 'forums/topic_create.html'

    topics = Topic.objects.all()
    topic_form = TopicForm()
    if request.method == "POST":
        topic_form = TopicForm(request.POST)
        if topic_form.is_valid():
            topic = topic_form.save()
            messages.success(request, "Topic <strong>%s</strong> was created" % (topic.title))
            return redirect(topic.get_absolute_url())

    ctx['topic_form'] = topic_form
    return render(request, template_name, ctx)

def topic_view_by_slug(request, slug):
    """
    redirects to bid-based view
    """
    topic = Topic.objects.get(slug=slug)
    return redirect(reverse('forums:view', kwargs={'bid': int_to_base36(topic.id)}))

@staff_member_required
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

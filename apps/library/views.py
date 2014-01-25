# encoding: utf-8

from django.shortcuts import render, redirect
from django.utils.http import base36_to_int, int_to_base36
from django.core.urlresolvers import reverse

from library.models import Resource

def resource_list(request):
    ctx = {}
    template_name = 'library/resource_list.html'

    resources = Resource.objects.all()
    ctx['resources'] = resources

    return render(request, template_name, ctx)

def resource_view_by_slug(request, slug):
    """
    redirects to bid-based view
    """
    resource = Resource.objects.get(slug=slug)
    return redirect(reverse('library:view', kwargs={'bid': int_to_base36(Resource.id)}))

def resource_view(request, bid):
    """
    List the topic at the top and disply replies
    """
    ctx = {}
    template_name = 'library/resource_view.html'

    resource = Resource.objects.get(id=base36_to_int(bid))
    ctx['topic'] = topic

    return render(request, template_name, ctx)

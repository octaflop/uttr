#encoding: utf-8

import datetime

from profiles.models import UttrUser

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from blog.forms import BlogForm
from blog.models import BlogPost

@login_required
def create(request):
    """
    Blog creation templates
    """
    ctx = {}
    ctx['compose_active'] = True
    template_name = 'blog/pm/create.html'

    blog_form = BlogForm(initial={'author': request.user})
    ctx['blog_form'] = blog_form

    if request.method == 'POST':
        blog_form = BlogForm(request.POST, initial={'author': request.user})
        ctx['blog_form'] = blog_form

        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            blog.author = request.user
            blog.save()
            message = "Your post was saved successfully!"
            messages.success(request, message)

        else:
            message = "Sorry, there was an issue with your post"
            messages.error(request, message)


    return render_to_response(template_name, RequestContext(request, ctx))

@login_required
def pm_list(request):
    ctx = {}
    ctx['pms'] = True
    template_name = 'blog/pm/list.html'
    library_entries = BlogPost.objects.filter(post_type='lib')
    ctx['library_entries'] = library_entries

    return render_to_response(template_name, ctx)
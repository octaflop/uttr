#encoding: utf-8

from django.shortcuts import render, render_to_response
from django.template import RequestContext

from blog.forms import BlogForm

def create(request):
    """
    Blog creation templates
    """
    ctx = {}
    template_name = 'blog/manage/create.html'

    blog_form = BlogForm()
    ctx['blog_form'] = blog_form

    return render_to_response(template_name, RequestContext(request, ctx))
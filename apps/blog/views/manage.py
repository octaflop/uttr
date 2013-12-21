#encoding: utf-8

from django.shortcuts import render, render_to_response

def create(request):
    """
    Blog creation templates
    """
    ctx = {}
    template_name = 'blog/manage/create.html'

    return render_to_response(template_name, ctx)
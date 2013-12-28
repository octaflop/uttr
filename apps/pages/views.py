# encoding: utf-8

from django.shortcuts import render_to_response

def code_of_conduct(request):
    template = 'pages/code_of_conduct.html'
    ctx = {}
    return render_to_response(template, ctx)

def about(request):
    template = 'pages/about.html'
    ctx = {}
    return render_to_response(template, ctx)

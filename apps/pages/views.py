# encoding: utf-8

from django.shortcuts import render


def code_of_conduct(request):
    template = 'pages/code_of_conduct.html'
    ctx = {}
    return render(request, template, ctx)


def about(request):
    template = 'pages/about.html'
    ctx = {}
    return render(request, template, ctx)

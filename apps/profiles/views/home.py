# encoding: utf-8

from django.shortcuts import render, get_object_or_404

def login(request):
    ctx = {}

    return render(request, 'profiles/login.html', ctx)

def index(request):
    ctx = {}

    return render(request, 'profiles/index.html', ctx)

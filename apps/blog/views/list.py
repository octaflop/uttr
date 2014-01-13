#encoding: utf-8

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from blog.models import BlogPost, ForumThread

@login_required
def library_list(request):
    ctx = {}
    ctx['lib_active'] = True
    template_name = 'blog/library/list.html'
    library_entries = BlogPost.objects.filter(post_type='lib')
    ctx['library_entries'] = library_entries

    return render(request, template_name, ctx)


@login_required
def library_entry(request, id):
    ctx = {}
    ctx['lib_active'] = True
    template_name = 'blog/library/entry.html'
    entry = BlogPost.objects.get(id=id, post_type='lib')
    ctx['entry'] = entry

    return render(request, template_name, ctx)


@login_required
def discussion_list(request):
    ctx = {}
    template_name = 'blog/forum/list.html'
    library_entries = BlogPost.objects.filter(post_type='disc')
    ctx['topics'] = library_entries

    return render(request, template_name, ctx)


@login_required
def discussion_entry(request, id):
    ctx = {}
    template_name = 'blog/forum/view.html'
    thread = ForumThread.objects.get(id=id)
    posts = thread.blogpost_set.all()
    ctx['thread'] = thread
    ctx['posts'] = posts

    return render(request, template_name, ctx)


@login_required
def pm_list(request):
    ctx = {}
    template_name = 'blog/library/list.html'
    library_entries = BlogPost.objects.filter(post_type='pm')
    ctx['library_entries'] = library_entries

    return render(request, template_name, ctx)


@login_required
def pm_entry(request, id):
    ctx = {}
    template_name = 'blog/library/entry.html'
    entry = BlogPost.objects.get(id=id, post_type='pm')
    ctx['entry'] = entry

    return render(request, template_name, ctx)


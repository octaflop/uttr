#encoding: utf-8

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from blog.models import BlogPost, ForumThread

from blog.forms import ReplyForm

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
    topic = thread.blogpost_set.all()[0]
    replies = thread.blogpost_set.filter(author__role='author', status='posted')
    ctx['thread'] = thread
    ctx['topic'] = topic
    ctx['replies'] = replies
    ctx['reply_form'] = ReplyForm()

    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        ctx['reply_form'] = reply_form
        if reply_form.is_valid:
            reply = reply_form.save(commit=False)
            reply.author = request.user
            reply.save()


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


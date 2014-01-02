#encoding: utf-8

import datetime

from profiles.models import UttrUser

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from blog.forms import PMForm
from blog.models import BlogPost

from postal.utils import mail_moderator

@login_required
def create(request):
    """
    Blog creation templates
    """
    ctx = {}
    ctx['compose_active'] = True
    template_name = 'blog/pm/create.html'

    blog_form = PMForm(initial={'author': request.user})
    ctx['blog_form'] = blog_form

    if request.method == 'POST':
        blog_form = PMForm(request.POST, initial={'author': request.user})
        ctx['blog_form'] = blog_form

        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            blog.publish_date = datetime.datetime.now()
            blog.author = request.user
            blog.post_type = 'pm'
            blog.status = 'posted'
            blog.entry = blog.draft
            blog.save()
            subject = "Private message sent via online interface"
            message = """
            You've received a message via the online interface.\n
            Message: \n
            %s

            Link to message: https://digitaltextbookstudy.com/admin/blog/blogpost/%s/
            """ % (blog.draft, blog.id)
            mail_moderator(subject, message)
            message = "Your message was sent successfully!"
            messages.success(request, message)
        else:
            message = "Sorry, there was an issue with your message"
            messages.error(request, message)


    return render_to_response(template_name, RequestContext(request, ctx))

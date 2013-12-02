# encoding: utf-8

from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from profiles.forms import LoginForm
from profiles.models import UttrUser

def login(request):
    ctx = {}
    login_form = LoginForm()
    ctx['login_form'] = login_form

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        ctx['login_form'] = login_form
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            try:
                user = UttrUser.objects.get(email=email)
            except UttrUser.DoesNotExist:
                return render(request, 'profiles/login.html', ctx)

            if not user.check_password(password):
                return render(request, 'profiles/login.html', ctx)

            return redirect(reverse('profiles:home'))

    return render(request, 'profiles/login.html', ctx)

def index(request):
    ctx = {}

    return render(request, 'profiles/index.html', ctx)

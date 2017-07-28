# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate

from django.template import loader

from .models import Post, User
from .forms import UserForm


# Create your views here.
def index(request):
    
    latest_post = Post.objects.order_by('-created')
    context = {
        'latest_post' : latest_post
    }
    
    return render(request, 'myApp/index.html', context)

def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    post = user.post_set.all()
    post = list(reversed(post))
    return render(request, 'myApp/user.html', {'user': user, 'post': post})

def user_all(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    post = user.post_set.all()
    post = list(reversed(post))
    return render(request, 'myApp/user.html', {'user': user, 'post': post})

def details(request, itemNum):
    item = get_object_or_404(Post, pk=itemNum)
    return render(request, 'myApp/details.html', {'item': item})
    
def filterCon(request, filterNum):
    resultList = Post.objects.filter(condition=filterNum)
    return render(request, 'myApp/filterRes.html',{'item_list': resultList})


def filterType(request, filterNum):
    resultList = Post.objects.filter(type1=filterNum)
    return render(request, 'myApp/filterRes.html',{'item_list': resultList})

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    return render(request, 'myApp/login.html', {'form': form})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                latest_post = Post.objects.order_by('-created')
                return render(request, 'myApp/index.html', {'latest_post' : latest_post})
            else:
                return render(request, 'myApp/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'myApp/login.html', {'error_message': 'Invalid login'})
    return render(request, 'myApp/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user =form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('myApp:index')
    return render(request, 'myApp/registration.html', {'form': form})
                    
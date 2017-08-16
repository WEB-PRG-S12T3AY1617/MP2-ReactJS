# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.views import generic
from django.http import HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from django.views.generic import View
from .models import Post, User, Offer
from .forms import UserForm, UploadForm, OfferForm

IMAGE_FILE_TYPES =['png', 'jpg', 'jpeg']

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
    latest_post = Post.objects.order_by('-created')
    return render(request, 'myApp/index.html', {'latest_post':latest_post})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                latest_post = Post.objects.order_by('-created')
                return redirect('myApp:index')
            else:
                return render(request, 'myApp/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'myApp/login.html', {'error_message': 'Invalid login'})
    return render(request, 'myApp/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
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

def upload_file(request):
    form = UploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.username = request.user
        post.image = request.FILES['image']
        file_type = post.image.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_FILE_TYPES:
            context = {
            'post': post,
             'form': form,
            'error_message': 'Image file must be PNG, JPG, or JPEG',
            }
            return render(request, 'myApp/upload.html', context)
        post.save()
        return redirect('myApp:index')
    return render(request, 'myApp/upload.html', {'form':form})

class OfferView(View):
    form_class = OfferForm
    template_name = 'myApp/offer.html'

    def get(self, request):
        if request.user.is_authenticated() and 'post' in request.GET:
            offer = None
            user = request.user
            try:
                offer = Offer.objects.get(userOffer=user)
                self.form_class = self.form_class = OfferForm(instance=offer, user=request.user)
            except ObjectDoesNotExist:
                self.form_class = OfferForm(user=request.user)

            return render(request, self.template_name, {'form': self.form_class, 'offer': offer})
        else:
            return HttpResponseRedirect('/myApp/')
        
    def post(self, request):
        if request.user.is_authenticated():
            try:
                post = Post.objects.get(id=request.POST['item'])
                user = request.user

                try:
                    offer = Offer.objects.get(item=post, userOffer=user)
                    form = OfferForm(data=request.POST, instance=offer)

                    if form.is_valid():
                        post = form.save(commit=False)
                        post.save()
                    else:
                        return render(request, self.template_name, {'form': form})
                except ObjectDoesNotExist:
                    offer = OfferForm(data=request.POST, user=user)

                    if offer.is_valid():
                        offer = offer.save(commit=False)
                        offer.item = post
                        offer.username = user
                        offer.save()
                    else:
                        return render(request, self.template_name, {'form': offer})

                return HttpResponseRedirect('/myApp/')
            except Post.DoesNotExist:
                return HttpResponseRedirect('/myApp/')
        else:
            return HttpResponseRedirect('/myApp/')
                  
def seeOffer(request, user_id):
    if request.user.is_authenticated():
        user = get_object_or_404(User, pk=user_id)
        post = Post.objects.filter(username=user)
        offers_list = Offer.objects.filter(item__in=post)
        return render(request, 'myApp/seeOffer.html', {'offers_list': offers_list})
    else:
        return HttpResponseRedirect('/myApp/')

def offerAccept(request):
    if request.user.is_authenticated():
        offer = Offer.objects.get(id=request.GET['offer'])
        offer.reject = False
        offer.accept = True
        offer.save()

        return HttpResponseRedirect('/myApp/')
    else:
        return HttpResponseRedirect('/myApp/')


def offerReject(request):
    if request.user.is_authenticated():
        try:
            offer = Offer.objects.get(id=request.GET['offer'])
            offer.reject = True
            offer.accept = False
            offer.save()

            return HttpResponseRedirect('/myApp/')
        except Offer.DoesNotExist:
            return HttpResponseRedirect('/myApp/')
    else:
        return HttpResponseRedirect('/myApp/')
    
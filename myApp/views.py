from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Item, Post, User

def index(request):
    latest_post = Post.objects.order_by('-created')[:10]
    context = {
        'latest_post' : latest_post
    }
    
    return render(request, 'myApp/index.html', context)

def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'myApp/item.html', {'item': item})

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myApp/post.html', {'post': post})

def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'myApp/user.html', {'user': user})
    
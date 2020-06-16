from django.shortcuts import render
from .models import Post
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    hello = 'Hello Chel!'
    number = 42
    return render(request, 'blog/index.html', context={'posts':posts,'number':number})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact = slug)
    return render(request, 'blog/post_detail.html', context={'post':post})
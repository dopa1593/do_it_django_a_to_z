from django.shortcuts import render
from .models import Post


# Create your views here.

def index(request):
    return render(
        request,
        'blog/index.html',
    )
def posts(request):
    posts = Post.objects.all()
    return render(
        request,
        'blog/post_list.html',
        {
            'posts': posts,
        }
    )
def info(request):
    return render(
        request,
        'blog/info.html'
    )
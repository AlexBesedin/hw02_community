from django.shortcuts import render, get_object_or_404
from .models import Post, Group

NUMBER_POSTS: int = 10


def index(request):
    posts = Post.objects.all()[:NUMBER_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:NUMBER_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)

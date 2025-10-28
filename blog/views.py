from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import Http404

# Create your views here.

def blog(request):
    context = {
        #'text': 'Ola Blog',
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def post(request, post_id):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

        if found_post is None:
            raise Http404('Post nao existe')

    context = {
        'post': found_post,
        'title':found_post['title'] + ' - ',
    }
    return render(request, 'blog/post.html', context)
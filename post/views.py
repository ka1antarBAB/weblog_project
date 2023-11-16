from django.shortcuts import render
from .models import Post
# Create your views here.


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "post/posts_list.html", {"posts_list": posts})


def post_detail_view(request, pk):
    posts = Post.objects.get(pk=pk)
    return render(request, "post/post_detail.html", {"post_detail": posts})

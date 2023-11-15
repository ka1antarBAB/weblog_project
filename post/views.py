from django.shortcuts import render
from .models import Post
# Create your views here.


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "post/posts_list.html", {"posts_list": posts})

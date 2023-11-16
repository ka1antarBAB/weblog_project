from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
# Create your views here.


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "post/posts_list.html", {"posts_list": posts})


def post_detail_view(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    # try:
    #     posts = Post.objects.get(pk=pk)
    # except Post.DoesNotExist as error:
    #     posts = None
    #     print(error)
    return render(request, "post/post_detail.html", {"post_detail": posts})

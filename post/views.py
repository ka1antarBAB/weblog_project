from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# Create your views here.

from .models import Post
from .forms import NewPostForm


def post_list_view(request):
    posts = Post.objects.filter(status="pub")
    return render(request, "post/posts_list.html", {"posts_list": posts})


def post_detail_view(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    # try:
    #     posts = Post.objects.get(pk=pk)
    # except Post.DoesNotExist as error:
    #     posts = None
    #     print(error)
    return render(request, "post/post_detail.html", {"post_detail": posts})


def post_add_view(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            form = NewPostForm
    else:
        form = NewPostForm()

    return render(request, "post/post_create.html", {"form": form})
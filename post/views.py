from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import redirect
# Create your views here.

from .models import Post
from .forms import NewPostForm


def post_list_view(request):
    posts = Post.objects.filter(status="pub").order_by("date_and_time_modified")
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
            return redirect("post_list_view")
    else:
        form = NewPostForm()
    return render(request, "post/post_create.html", {"form": form})


def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = NewPostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect("post_list_view")
    return render(request, "post/post_create.html", {"form": form})


def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("post_list_view")
    return render(request, "post/post_delete.html", {"post":post})


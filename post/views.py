from django.shortcuts import render, HttpResponse
from . models import Post
# Create your views here.


def post_list_view(request):
    post = Post.objects.all()
    context = {
        "post": post
    }
    return render(request, "post/list_view.html", context=post)

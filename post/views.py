from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import reverse

from .models import Post
from .forms import NewPostForm


class PostListView(generic.ListView):
    template_name = "post/posts_list.html"
    context_object_name = "posts_list"

    def get_queryset(self):
        return Post.objects.filter(status="pub").order_by("date_and_time_modified")


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post/post_detail.html"
    context_object_name = "post_detail"


class PostCreateView(generic.CreateView):
    form_class = NewPostForm
    template_name = "post/post_create.html"


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = "post/post_create.html"


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "post/post_delete.html"
    success_url = reverse_lazy("post_list_view")
    # or
    # def get_success_url(self):
    #     return reverse("post_list_view")

# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from django.shortcuts import redirect

# def post_list_view(request):
#     posts = Post.objects.filter(status="pub").order_by("date_and_time_modified")
#     return render(request, "post/posts_list.html", {"posts_list": posts})

# def post_detail_view(request, pk):
#     posts = get_object_or_404(Post, pk=pk)
#     # try:
#     #     posts = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist as error:
#     #     posts = None
#     #     print(error)
#     return render(request, "post/post_detail.html", {"post_detail": posts})

# def post_add_view(request):
#     if request.method == "POST":
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = NewPostForm
#             return redirect("post_list_view")
#     else:
#         form = NewPostForm()
#     return render(request, "post/post_create.html", {"form": form})

# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         post.delete()
#         return redirect("post_list_view")
#     return render(request, "post/post_delete.html", {"post": post})

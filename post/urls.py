from django.urls import path
from .import views


urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list_view"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post_detail_view"),
    path("add/", views.PostCreateView.as_view(), name="post_create_view"),
    path("<int:pk>/update/", views.PostUpdateView.as_view(), name="post_update_view"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete_view"),

]

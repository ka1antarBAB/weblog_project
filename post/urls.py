from django.urls import path
from .import views


urlpatterns = [
    path("", views.post_list_view, name=""),
    path("<int:pk>/", views.post_detail_view, name="post_detail_view"),
    path("add/", views.post_add_view, name="post_add_view")
]

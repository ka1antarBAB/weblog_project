from django.urls import path
from .import views


urlpatterns = [
    path("", views.post_list_view, name="list_view"),
    path("<int:pk>/", views.post_detail_view, name="detail_view")
]

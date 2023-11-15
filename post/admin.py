from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "author", "date_and_time_modified"]
    ordering = ("-status", )



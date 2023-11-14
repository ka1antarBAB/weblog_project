from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "author", "date_and_time_modified"]
    ordering = ("-status", )


admin.site.register(Post, PostAdmin)


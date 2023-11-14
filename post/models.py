from django.db import models
from django.contrib import auth


# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ("pub", "Published"),
        ("drf", "Draft")
    )
    text = models.CharField(max_length=100)
    title = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    date_and_time_created = models.DateTimeField(auto_now_add=True)
    date_and_time_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)



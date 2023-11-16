from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your tests here.
class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="userCheck"
        )
        self.post = Post.objects.create(
            title="title check",
            text="text check",
            status=Post.STATUS_CHOICES[0][0],
            author=self.user,
        )

    def test_post_list_url(self):
        response = self.client.get(reverse("post_list_view"))
        self.assertEquals(response.status_code, 200)

    def test_post_list_by_name(self):
        response = self.client.get("/blog/")
        self.assertEquals(response.status_code, 200)


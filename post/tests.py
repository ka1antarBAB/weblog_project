from django.test import TestCase
from django.contrib.auth.models import User

from django.shortcuts import reverse

from .models import Post


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
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_post_list_by_name(self):
        response = self.client.get(reverse("post_list_view"))
        self.assertEqual(response.status_code, 200)

    def test_post_title_text_author_on_post_list(self):
        response = self.client.get(reverse("post_list_view"))
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.text)
        self.assertContains(response, self.post.author)

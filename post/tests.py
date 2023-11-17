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
        self.post2 = Post.objects.create(
            title="title post2 check",
            text="text post2 check",
            status=Post.STATUS_CHOICES[1][0],
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

    def test_post_detail_url(self):
        response = self.client.get(f"/blog/{self.post.id}/")
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.text)
        self.assertContains(response, self.post.author)

    def test_post_detail_by_name(self):
        response = self.client.get(reverse("post_detail_view", args=[self.post.id]))
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.text)
        self.assertContains(response, self.post.author)

    def test_post_does_not_exits_404_error(self):
        response = self.client.get(reverse("post_detail_view", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_view_renders_correct_template_for_post_list(self):
        response = self.client.get(reverse("post_list_view"))
        self.assertTemplateUsed(response, template_name="post/posts_list.html")

    def test_view_renders_correct_template_for_post_detail(self):
        response = self.client.get(reverse("post_detail_view", args=[self.post.id]))
        self.assertTemplateUsed(response, template_name="post/post_detail.html")

    def test_draft_post_not_show(self):
        response = self.client.get(reverse("post_list_view"))
        self.assertNotContains(response, self.post2.title)
        self.assertNotContains(response, self.post2.text)



from django.test import TestCase

# Create your tests here.


class TestPostsViews(TestCase):

    def test_blogpost_view(self):
        page = self.client.get('/posts/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'blogposts.html')


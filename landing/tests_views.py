from django.test import TestCase


# Create your tests here.
class TestLandingView(TestCase):

    def test_landing_page_view(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')

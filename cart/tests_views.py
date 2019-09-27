from django.test import TestCase


# Create your tests here.
class TestCartViews(TestCase):

    def test_cart_view(self):
        page = self.client.get('/cart/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')

from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
class TestCheckoutView(TestCase):

    def test_checkout_view(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')

        page = self.client.get('/checkout/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'checkout.html')

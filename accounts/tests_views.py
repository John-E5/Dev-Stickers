from django.contrib.auth.models import User
from django.test import TestCase


class TestAccountViews(TestCase):

    def test_register_view(self):
        page = self.client.get('/accounts/register/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'register.html')

    def test_login_view(self):
        page = self.client.get('/accounts/login/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')

    def test_logout_view(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')

    def test_profile_page_view(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        page = self.client.get('/accounts/profile/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'profile.html')


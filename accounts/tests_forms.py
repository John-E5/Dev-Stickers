from django.test import TestCase
from .forms import UserRegistrationForm


# Create your tests here.
class TestAccountsForms(TestCase):

    def test_user_creation(self):
        data = {
            'username': 'testclient',
            'email': 'test@test.com',
            'password1': 'test123',
            'password2': 'test123',
        }
        form = UserRegistrationForm(data)
        self.assertTrue(form.is_valid())

    def test_empty_user_name(self):
        form = UserRegistrationForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    def test_cant_register_with_just_username(self):
        form = UserRegistrationForm({'username': 'New User'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password1'], [u'This field is required.'])

    def test_passwords_must_match(self):
        data = {
            'password1': 'test123',
            'password2': 'test112',
        }

        form = UserRegistrationForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'Passwords do not match'])

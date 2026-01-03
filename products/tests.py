from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.

class SuperuserRequiredTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('normal', 'normal@test.com', 'pass')
        self.superuser = User.objects.create_superuser('admin', 'admin@test.com', 'pass')

    def test_non_superuser_redirected(self):
        self.client.login(username='normal', password='pass')
        response = self.client.get(reverse('delete_product', args=[1]))
        self.assertRedirects(response, reverse('home'))

    def test_superuser_allowed(self):
        self.client.login(username='admin', password='pass')
        response = self.client.get(reverse('delete_product', args=[1]))
        self.assertNotEqual(response.status_code, 302)

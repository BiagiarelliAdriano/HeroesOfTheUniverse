from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class LandingPageTests(TestCase):
    def test_landing_page_title_displayed(self):
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Heroes Of The Universe")

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_redirect_to_home_if_logged_in(self):
        self.client.force_login(self.user)
        
        response = self.client.get(reverse('landing'))

        self.assertRedirects(response, reverse('main_home:home'))
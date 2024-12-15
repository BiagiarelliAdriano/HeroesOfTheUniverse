from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class LandingPageTests(TestCase):
    def test_landing_page_title_displayed(self):
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Heroes Of The Universe")
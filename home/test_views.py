from  django.test import TestCase
from django.urls import reverse

class HomeLandingPageTest(TestCase):

    def test_view_url_exists(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_access_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
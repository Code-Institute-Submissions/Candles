from django.test import TestCase
from django.urls import reverse

from shop.views import *

class ShopViewTest(TestCase):

    def test_correct_shop_view_page_displayed_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_shop_view_url_accesible_by_name(self):
        response = self.client.get(reverse('displayShop'))
        self.assertEqual(response.status_code, 200)

    def test_correct_shop_view_template_used(self):
        response = self.client.get(reverse('displayShop'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/store.html')
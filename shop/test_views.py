from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import render
from django.template.response import TemplateResponse

from shop.views import *
from products.models import *

class ShopViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        product_test = Product.objects.create(name='New Candle',
            description='A description', price='45.00',
            top_note_1='Lavender', top_note_2='Mint',
            heart_note_1='Bergamot', base_note_1='Oud',
            stripe_id='StripeID10')
        product_test.save()

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

    def test_correct_product_view_display_at_desired_location(self):
        response = self.client.get('/shop/1/')
        self.assertEqual(response.status_code, 200)

    def test_product_view_url_accesible_by_name(self):
        response = self.client.get(reverse('displayProduct', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_correct_product_view_template_used(self):
        response = self.client.get(reverse('displayProduct', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/displayProduct.html')

    def test_correct_products_returned_for_display_shop_view(self):
        product = Product.objects.get(id=1)
        response = self.client.get(reverse('displayShop'))
        self.assertTrue(product.name=='New Candle')
        self.assertTrue(product.price==45.00)
        
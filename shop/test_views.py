from django.test import TestCase
from products.models import Product

class TestViews(TestCase):
    
    def test_get_home_landing_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_shop_landing_page(self):
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/store.html')

    def test_get_about_and_contact_page(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/email.html')

    def test_get_member_area_page(self):
        response = self.client.get('/account/memberarea/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/memberArea.html')

    def test_get_individual_product_page(self):
        item = Product.objects.create(id='78', price=39)
        response = self.client.get(f'/shop/{item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/displayProduct.html')

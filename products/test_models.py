from django.test import TestCase

from .models import Product

class TestProductModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name='Candle',
            description='A candle description', price='39.00',
            top_note_1='Lavender', top_note_2='Mint',
            heart_note_1='Bergamot', base_note_1='Oud',
            stripe_id='StripeID01')
    #'name tests'
    def test_name_of_product(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_value_of_product(self):
        product = Product.objects.get(id=1)
        name_value = product.name
        self.assertEquals(name_value, 'Candle')

    def test_name_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 254)
        
    #'description tests
    def test_description_of_product(self):
        product = Product.objects.get(id=1)
        description_label = product._meta.get_field('description').verbose_name
        self.assertEquals(description_label, 'description')

    def test_description_value_of_product(self):
        product = Product.objects.get(id=1)
        description_value = product.description
        self.assertEquals(description_value, 'A candle description')


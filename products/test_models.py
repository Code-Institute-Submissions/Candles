from django.test import TestCase
from decimal import *
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
        
    #description tests
    def test_description_of_product(self):
        product = Product.objects.get(id=1)
        description_label = product._meta.get_field('description').verbose_name
        self.assertEquals(description_label, 'description')

    def test_description_value_of_product(self):
        product = Product.objects.get(id=1)
        description_value = product.description
        self.assertEquals(description_value, 'A candle description')

    #price tests
    def test_price_of_product(self):
        product = Product.objects.get(id=1)
        price_label = product._meta.get_field('price').verbose_name
        self.assertEquals(price_label, 'price')

    def test_price_value_of_product(self):
        product = Product.objects.get(id=1)
        price_value = product.price
        self.assertEquals(price_value, Decimal(39))

    #top_note_1 tests
    def test_name_of_top_note_1(self):
        product = Product.objects.get(id=1)
        top_note_1_label = product._meta.get_field('top_note_1').verbose_name
        self.assertEquals(top_note_1_label, 'top note 1')

    def test_name_value_of_top_note_1(self):
        product = Product.objects.get(id=1)
        top_note_1_value = product.top_note_1
        self.assertEquals(top_note_1_value, 'Lavender')

    def test_top_not_1_max_length(self):
        product = Product.objects.get(id=1)
        top_note_1_max_length = product._meta.get_field('top_note_1').max_length
        self.assertEquals(top_note_1_max_length, 254)

    #top_note_2 tests
    def test_name_of_top_note_2(self):
        product = Product.objects.get(id=1)
        top_note_2_label = product._meta.get_field('top_note_2').verbose_name
        self.assertEquals(top_note_2_label, 'top note 2')

    def test_name_value_of_top_note_1(self):
        product = Product.objects.get(id=1)
        top_note_2_value = product.top_note_2
        self.assertEquals(top_note_2_value, 'Mint')

    def test_top_note_2_max_length(self):
        product = Product.objects.get(id=1)
        top_note_2_max_length = product._meta.get_field('top_note_2').max_length
        self.assertEquals(top_note_2_max_length, 254)

    #heart_note_1 tests
    def test_name_of_heart_note_1(self):
        product = Product.objects.get(id=1)
        heart_note_1_label = product._meta.get_field('heart_note_1').verbose_name
        self.assertEquals(heart_note_1_label, 'heart note 1')

    def test_name_value_of_heart_note_1(self):
        product = Product.objects.get(id=1)
        heart_note_1_value = product.heart_note_1
        self.assertEquals(heart_note_1_value, 'Bergamot')

    def test_heart_note_1_max_length(self):
        product = Product.objects.get(id=1)
        heart_note_1_max_length = product._meta.get_field('heart_note_1').max_length
        self.assertEquals(heart_note_1_max_length, 254)

    #base_note_1 tests
    def test_name_of_base_note_1(self):
        product = Product.objects.get(id=1)
        base_note_1_label = product._meta.get_field('base_note_1').verbose_name
        self.assertEquals(base_note_1_label, 'base note 1')

    def test_name_value_of_base_note_1(self):
        product = Product.objects.get(id=1)
        base_note_1_value = product.base_note_1
        self.assertEquals(base_note_1_value, 'Oud')

    def test_base_note_1_max_length(self):
        product = Product.objects.get(id=1)
        base_note_1_max_length = product._meta.get_field('base_note_1').max_length
        self.assertEquals(base_note_1_max_length, 254)

    #stripe_id tests
    def test_name_of_stripe_id(self):
        product = Product.objects.get(id=1)
        stripe_id_label = product._meta.get_field('stripe_id').verbose_name
        self.assertEquals(stripe_id_label, 'stripe id')

    def test_name_value_of_stripe_id(self):
        product = Product.objects.get(id=1)
        stripe_id_value = product.stripe_id
        self.assertEquals(stripe_id_value, 'StripeID01')

    def test_stripe_id_max_length(self):
        product = Product.objects.get(id=1)
        stripe_id_max_length = product._meta.get_field('stripe_id').max_length
        self.assertEquals(stripe_id_max_length, 254)

    #__str__ test
    def test_str_method(self):
        product = Product.objects.get(id=1)
        self.assertTrue(isinstance(product, Product))
        expected_object_name = f'{product.name}'
        self.assertEqual(expected_object_name, str(product))
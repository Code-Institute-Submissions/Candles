from django.test import TestCase
from .models import Review
from products.models import Product

class TestProductModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name='Candle2',
            description='A candle description', price='45.00',
            top_note_1='Lavender', top_note_2='Mint',
            heart_note_1='Bergamot', base_note_1='Oud',
            stripe_id='StripeID01')

    
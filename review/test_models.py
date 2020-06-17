from django.test import TestCase
from .models import Review

class TestProductModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        
    #'name tests'
    def test_name_of_product(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
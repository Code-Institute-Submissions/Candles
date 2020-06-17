import datetime

from django.test import TestCase
from .models import Review
from products.models import Product
from django.utils import timezone
from django.contrib.auth.models import User

class TestProductModel(TestCase):
    @classmethod
    def setUpTestData(self):
        user1 = User.objects.create_user(username='testuser1', password='1Xuyty89iu8')
        user1.save()
        
        product1 = Product.objects.create(name='Discover',
            description='A brief description', price='40.00',
            top_note_1='Lavender', top_note_2='Mint',
            heart_note_1='Bergamot', base_note_1='Oud',
            stripe_id='StripeID05')
        product1.save()

        review1 = Review.objects.create(user=user1, product=product1, date=timezone.now(), review_title='This is a title', review_text='This is the review text')
        review1.save()

    def test_review_title_label(self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('review_title').verbose_name
        self.assertEquals(field_label, 'review title')

    def test_review_text_label(self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('review_text').verbose_name
        self.assertEquals(field_label, 'review text')

    def test_review_user_referenced_correctly(self):
        review = Review.objects.get(id=1)
        reviewer = review._meta.get_field('user')
        self.assertTrue(reviewer, 'testuser1')

    def test_str_method(self):
        review = Review.objects.get(id=1)
        reviewer = review._meta.get_field('user')
        expected_string = f'Review for user {reviewer}'
        self.assertTrue(expected_string, 'Review for user testuser1')

    
    
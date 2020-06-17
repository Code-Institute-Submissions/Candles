import datetime

from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from products.models import Product
from .models import Review
from .views import *

class TestReviewViews(TestCase):
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

    def test_correct_review_page_displayed_at_desired_location(self):
        login = self.client.login(username='testuser1', password='1Xuyty89iu8')
        response = self.client.get('/review/')
        self.assertEqual(response.status_code, 200)

    def test_shop_view_url_accesible_by_name(self):
        login = self.client.login(username='testuser1', password='1Xuyty89iu8')
        response = self.client.get(reverse('writeAReview'))
        self.assertEqual(response.status_code, 200)

    def test_correct_shop_view_template_used(self):
        login = self.client.login(username='testuser1', password='1Xuyty89iu8')
        response = self.client.get(reverse('writeAReview'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review/displayWriteReview.html')

    def test_write_a_review_page_cannot_be_accessed_if_not_logged_in(self):
        response = self.client.get('/review/')
        self.assertEqual(response.status_code, 302)

    def test_can_submit_review(self):
        login = self.client.login(username='testuser1', password='1Xuyty89iu8')
        data = {
            'user':'user1',
            'product':'product1',
            'date': timezone.now(),
            'review_title': 'A review title',
            'review_text':'The review text that goes on and on....'
        }
        response = self.client.post('/review/', data=data)
        self.assertEqual(response.status_code, 200)
        



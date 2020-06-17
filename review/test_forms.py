from django.test import TestCase
from .forms import ReviewForm

class ReviewFormTest(TestCase):
    def test_review_form_product_field_label(self):
        form_data = {'product':'Tester',
        'review_title':'Title', 'review_text':'This is the body of text.'}
        form = ReviewForm(data=form_data)
        self.assertTrue(form.fields['product'].label == 'Product')

    def test_review_title_form_field_label(self):
        form_data = {'product':'Tester',
        'review_title':'Title', 'review_text':'This is the body of text.'}
        form = ReviewForm(data=form_data)
        self.assertTrue(form.fields['review_title'].label == 'Review title')

    def test_review_text_form_product_field_label(self):
        form_data = {'product':'Tester',
        'review_title':'Title', 'review_text':'This is the body of text.'}
        form = ReviewForm(data=form_data)
        self.assertTrue(form.fields['review_text'].label == 'Review text')

    def test_review_form_invalid_no_product(self):
        form_data = {'product':'',
        'review_title':'Title', 'review_text':'This is the body of text.'}
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_review_form_invalid_no_title(self):
        form_data = {'product':'Tester',
        'review_title':'', 'review_text':'This is the body of text.'}
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_review_form_invalid_no_text(self):
        form_data = {'product':'Tester',
        'review_title':'Title', 'review_text':''}
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())

    

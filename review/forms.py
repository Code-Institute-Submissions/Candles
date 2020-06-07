from django import forms
from django.forms import ModelForm
from products.models import Product
from review.models import Review, ReviewForm, SCORE_CHOICES
from datetime import date

class ReviewForm(forms.Form):
    product = forms.ModelMultipleChoiceField(queryset=Product.objects.all())
    review_title = forms.CharField(max_length=100)
    review_text = forms.CharField(max_length=100, widget=forms.Textarea)
    score = forms.CharField(
        max_length=3,
        widget=forms.Select(choices=SCORE_CHOICES),
    )
    date = forms.DateField()
    user = forms.CharField(max_length=100)
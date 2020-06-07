from django import forms
from django.forms import ModelForm
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'review_title', 'review_text']
        

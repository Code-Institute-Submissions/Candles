from django.db import models
from django.forms import ModelForm, Textarea, CharField, DateField
from django.conf import settings
from django.contrib.auth.models import User
from products.models import Product

SCORE_CHOICES = [
    ('1', 'One'),
    ('2', 'Two'),
    ('3', 'Three'),
    ('4', 'Four'),
    ('5', 'Five'),
]   
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    review_title = models.CharField(max_length=100, blank=False)
    review_text = models.TextField(default='')
    score = models.CharField(max_length=3, choices=SCORE_CHOICES)

    def __str__(self):
        return f'Review for user {self.user.username}'

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'product', 'date', 'review_title', 'review_text', 'score']
        widgets = {
            'review_text': Textarea(attrs={'cols': 100, 'rows': 20}),
        }
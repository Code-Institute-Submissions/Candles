from django.db import models
from django.conf import settings
from products.models import Product

class Review(models.Model):
    REVIEW_SCORE = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    review_text = models.TextField(default='')
    review_score = models.CharField(max_length=1, choices=REVIEW_SCORE)

    def __str__(self):
        return f'Review for user {self.user.username}'